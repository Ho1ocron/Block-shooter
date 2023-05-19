import sqlite3


class User:
    def __init__(self):
        self.connection = sqlite3.connect('CRData.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS stats(
                            Cash INT,
                            Total_Cash INT
                            Time_Played INT,
                            Map_Complete INT,
                            Arrival_Complete INT,
                            Map_Open INT,
                            Car_Open INT,
                            Background_Open INT);""")
        q = self.cursor.execute("SELECT * FROM stats").fetchall()
        if q is None:
            self.cursor.execute("INSERT INTO stats('Cash', 'Total_Cash', 'Time_Played', 'Map_Complete', "
                                "'Arrival_Complete', 'Map_Open', 'Car_Open', 'Background_Open') VALUES(?, ?, ?, ?, ?,"
                                " ?, ?, ?)", (0, 0, 0, 0, 0, 0, 1, 1))
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
                            Car STR, 
                            Power REAL,
                            Clutch REAL,
                            Streamlining REAL,
                            Max_Speed REAL,
                            Price INT,
                            Structure STR);""")
        if not self.cursor.execute("SELECT * FROM cars").fetchall():
            self.cursor.execute("INSERT INTO cars('Car', 'Power', 'Clutch', 'Streamlining', 'Max_Speed', 'Price',"
                                "'Structure') VALUES(?, ?, ?, ?, ?, ?, ?)", ('Lada Kalina', 1.0, 1.0, 1.0, 7.0, 0,
                                                                             'car1.png'))
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS backgrounds(
                            Background STR,
                            Clutch REAL,
                            Price INT,
                            Structure STR);""")
        if not self.cursor.execute("SELECT * FROM backgrounds").fetchall():
            self.cursor.execute("INSERT INTO backgrounds('Background', 'Clutch', 'Price', 'Structure') VALUES(?, ?, ?,"
                                "?)", ('Ice 1', 1.2, 0, 'bg1.png'))
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS session(
                            GameMode STR,
                            Car STR,
                            Level STR,
                            Background STR);""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS maps(
                            map STR);""")

    def get_car(self, name):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM cars WHERE Structure = '{name}'").fetchall()

    def get_all_car(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM cars").fetchall()

    def get_background(self, background):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM backgrounds WHERE Structure = '{background}'").fetchall()

    def get_all_background(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM backgrounds").fetchall()

    def create_session(self, gm, car, level, bg):
        with self.connection:
            return self.cursor.execute("INSERT INTO session('GameMode', 'Car', 'Level', 'Background') VALUES(?, ?, ?,"
                                       "?)", (gm, car, level, bg))

    def get_session(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM session").fetchall()

    def create_map(self, name):
        self.cursor.execute(F"""CREATE TABLE IF NOT EXISTS {name}map(
                            id INT, type INT, width BIGINT, height BIGINT);""")
        with self.connection:
            return self.cursor.execute("INSERT INTO maps(map) VALUES(?)", name)
