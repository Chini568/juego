import sqlite3
class Sqlite:
    def save_score(self, player_name, final_score):
            connection = sqlite3.connect('Score.db')  
            cursor = connection.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player_name TEXT,
                    score INTEGER
                )
            ''')

            cursor.execute('INSERT INTO scores (player_name, score) VALUES (?, ?)', (player_name, final_score))

            connection.commit()
            connection.close()

    def order_score(self):
        connection = sqlite3.connect('Score.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM scores ORDER BY score DESC')
        ordered_scores = cursor.fetchall()

        cursor.execute('DELETE FROM scores')

        for score_record in ordered_scores:
            cursor.execute('INSERT INTO scores (player_name, score) VALUES (?, ?)', (score_record[1], score_record[2]))

        connection.commit()
        connection.close()

    def get_scores(self):
        connection = sqlite3.connect('Score.db')
        cursor = connection.cursor()

        cursor.execute('SELECT player_name, score FROM scores ORDER BY score DESC')
        scores = cursor.fetchall()

        connection.close()

        return scores