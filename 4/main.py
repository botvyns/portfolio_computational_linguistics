import sqlite3
from utils import execute_query, parse_text

def main():
    conn = sqlite3.connect('pol_lab07.s3db')
    cursor = conn.cursor()

    # First Query
    first_query = "SELECT sgN from tnoun LIMIT 1"
    result = execute_query(cursor, first_query)
    print(f"Результат виконання першого SQL-запиту: {result[0][0]}\n")

    # Second Query
    second_query = "SELECT sgL FROM tnoun WHERE sgL LIKE ?"
    result = execute_query(cursor, second_query, ('D%',))
    all_words = ', '.join(word[0] for word in result)
    print(f"Результат виконання другого SQL-запиту: {all_words}\n")

    # Third Query
    third_query = "INSERT INTO tnoun (sgN, gender) VALUES (?, ?)"
    execute_query(cursor, third_query, ('profesor', 1))
    conn.commit()

    # Parsing Text
    sgN, sgG, sgD, sgA, sgI, sgL, sgV, plN, plG, plD, plA, plI, plL, plV = parse_text("parse_lab07.txt")

    # Fourth Query
    fourth_query = """UPDATE tnoun SET sgN = ?, sgG = ?, sgD = ?, sgA = ?, sgI = ?, sgL = ?, sgV = ?,  plN = ?, plG = ?, plD = ?, plA = ?, plI = ?, plL = ?, plV = ?  WHERE sgN LIKE 'profesor'"""
    execute_query(cursor, fourth_query, (sgN[0], sgG[0], sgD[0], sgA[0], sgI[0], sgL[0], sgV[0], f"{plN[0]}, {plN[1]}", plG[0], plD[0], plA[0], plI[0], plL[0], f"{plV[0]}, {plV[1]}"))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()