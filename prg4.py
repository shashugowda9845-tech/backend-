from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Students
        SET name = ?, email = ?, age = ?
        WHERE id = ?
    """, (
        data["name"],
        data["email"],
        data.get("age", 0),
        student_id
    ))

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "student not found"}), 404

    conn.close()
    return jsonify({"message": "student updated"}), 200


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM Students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "student not found"}), 404

    conn.close()
    return jsonify({"message": "student deleted"}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
