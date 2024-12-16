from typing import Any

import psycopg2


def create_database(database_name: str, params: dict) -> None:
    """Создание базы данных и таблиц для сохранения данных о вакансиях и работодателях."""

    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE IF EXISTS {database_name}')
    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE employers (
                employer_id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id SERIAL PRIMARY KEY, 
                employer_id INT REFERENCES employers(employer_id), 
                name VARCHAR(255) NOT NULL,
                url VARCHAR(255),
                salary INTEGER
            )
        """)

    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict, employer_ids: dict) -> None:
    """Сохранение данных о работодателях и вакансиях в базу данных."""
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        for employer in employer_ids:

            cur.execute(
                """
                INSERT INTO employers (name)
                VALUES (%s)
                RETURNING employer_id
                """,
                employer_ids[employer]
            )
            employer_id = cur.fetchone()[0]
