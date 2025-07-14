from fastapi import APIRouter, Query
import sqlite3

router = APIRouter()
DB_PATH = "api/utils/outlets.db"

@router.get("/outlets")
async def query_outlets(query: str = Query(..., description="Ask about ZUS Coffee outlets")):
    if not query.strip():
        return {"error": "Empty query provided."}

    # Basic SQL injection filter (you can improve this further)
    if any(bad in query.lower() for bad in ["--", ";", "drop", " or ", "' or", "1=1"]):
        return {"error": "Invalid input detected. Please rephrase your query."}

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query_lower = query.lower()

        if "selangor" in query_lower:
            cursor.execute("SELECT * FROM outlets WHERE state LIKE ?", ("%Selangor%",))
        elif "how many" in query_lower:
            cursor.execute("SELECT COUNT(*) FROM outlets")
            count = cursor.fetchone()[0]
            return {"query": query, "answer": f"There are {count} outlets in the database."}
        else:
            cursor.execute("SELECT * FROM outlets")

        rows = cursor.fetchall()
        columns = ["id", "name", "state", "hours", "services"]
        formatted_results = [dict(zip(columns, row)) for row in rows]
        return {"query": query, "results": formatted_results}

    except Exception as e:
        return {"error": f"Server error: {str(e)}"}

    finally:
        try:
            conn.close()
        except:
            pass
