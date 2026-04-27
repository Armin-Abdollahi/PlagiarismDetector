import mysql.connector
from mysql.connector import Error
from database.queries import (
    CREATE_RESULTS_TABLE,
    INSERT_RESULT,
    SELECT_RESULT_BY_ID,
    SELECT_LATEST_RESULTS
)


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="plagiarism_db",
        charset="utf8mb4"
    )


def init_db():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(CREATE_RESULTS_TABLE)
        conn.commit()
    except Error:
        pass
    finally:
        if conn:
            conn.close()


def save_result(reference_text, suspect_text, scores):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            INSERT_RESULT,
            (
                reference_text,
                suspect_text,
                scores["lexical"],
                scores["semantic"],
                scores["structure"]
            )
        )
        conn.commit()
        return cur.lastrowid
    except Error:
        return None
    finally:
        if conn:
            conn.close()


def get_result_by_id(result_id):
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute(SELECT_RESULT_BY_ID, (result_id,))
        return cur.fetchone()
    except Error:
        return None
    finally:
        if conn:
            conn.close()


def get_latest_results(limit=10):
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute(SELECT_LATEST_RESULTS, (limit,))
        return cur.fetchall()
    except Error:
        return []
    finally:
        if conn:
            conn.close()
