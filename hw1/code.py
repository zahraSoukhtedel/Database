import psycopg2
from faker import Faker


def _create_authors_instances(count):
    fake = Faker()
    with open("temp.txt", "rb") as file:
        binary_data = file.read()
    instances = [
        (
            i,
            fake.name(),
            fake.boolean(),
            fake.date(),
            binary_data
        )
        for i in range(1, 1 + count)
    ]
    return instances


def _create_books_instances(count):
    fake = Faker()
    instances = [
        (
            i,
            fake.catch_phrase(),
            fake.boolean(),
            fake.date(),
            10 ** 6 - i + 1
        )
        for i in range(1, 1 + count)
    ]

    return instances


def main():
    sample_count = 10 ** 6
    conn = psycopg2.connect(database="homework1", user="postgres", password="", host="localhost", port="5432")
    cursor = conn.cursor()

    authors = _create_authors_instances(sample_count)
    cursor.executemany("INSERT INTO authors (id, full_name, sex, birth_date, avatar) VALUES (%s, %s, %s, %s, %s)",
                       authors)
    conn.commit()
    print("authors don!")
    books = _create_books_instances(sample_count)
    cursor.executemany("INSERT INTO books (id, title, is_published, created_at, author_id) VALUES (%s, %s, %s, %s, %s)",
                       books)
    conn.commit()
    print("books don!")
    conn.close()


if __name__ == '__main__':
    main()
