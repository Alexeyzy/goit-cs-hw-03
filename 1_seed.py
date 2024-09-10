from faker import Faker
import psycopg2

fake = Faker()

# Підключення 
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="alexeyb344",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Заповнення таблиці status
statuses = ['new', 'in progress', 'completed']
cur.executemany("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING;", [(status,) for status in statuses])

# Заповнення таблиці users
users = [(fake.name(), fake.unique.email()) for _ in range(10)]
cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT DO NOTHING;", users)

# Отримання id користувачів і статусів для використання в tasks
cur.execute("SELECT id FROM users")
user_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id FROM status")
status_ids = [row[0] for row in cur.fetchall()]

# Заповнення таблиці tasks
tasks = [
    (fake.sentence(nb_words=4), fake.paragraph(nb_sentences=3), status_ids[fake.random_int(min=0, max=len(status_ids)-1)], user_ids[fake.random_int(min=0, max=len(user_ids)-1)])
    for _ in range(20)
]
cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);", tasks)

conn.commit()
cur.close()
conn.close()

print("Таблиці заповнені.")
