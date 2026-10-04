from server.db import get_connection

def find_last_reserve(search_type: str, search_value):

    conn = get_connection()
    cursor = conn.cursor()
    try:
        if search_type == 'id':
            s_type = "a.id"
        elif search_type == 'collar_code':
            s_type = "a.collar_code"
        else:
            raise ValueError("Invalid search type")

        sql= f"""
        SELECT a.id AS animal_ID,a.collar_code,a.species,a.nickname,r.name AS reserve_name,
        r.region,r.description from animals a
        JOIN reserves r on r.id = a.last_seen_reserve_id
        WHERE {s_type} = %s
        """
        cursor.execute(sql, (search_value,))
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()
        conn.close()


