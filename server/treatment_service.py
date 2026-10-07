from server.db import get_connection

def create_treatment(outcome,animal_id,reserve_id,ranger_id,date):
    if outcome not in ["treated", "relocated","healthy"]:
        raise ValueError("Outcome must be 'treated' or 'relocated',healthy")
    if not animal_id or not reserve_id or not ranger_id or not date:
        raise ValueError("All fields are required")
    if not isinstance(animal_id, int) or not isinstance(reserve_id, int) or not isinstance(ranger_id, int):
        raise ValueError("Animal ID, Reserve ID and Ranger ID must be integers")
    if not isinstance(date, str):
        raise ValueError("Date must be a string")

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT '
                       'EXISTS(SELECT 1 FROM animals WHERE id = %s) AS animal_exists,'
                       'EXISTS(SELECT 1 FROM rangers WHERE id = %s) AS ranger_exists,'
                       'EXISTS(SELECT 1 FROM reserves WHERE id = %s) AS reserve_exists,'
                       'EXISTS(SELECT 1 FROM treatments WHERE animal_id = %s AND ranger_id = %s AND reserve_id = %s) AS treatment_exists',
                               (animal_id, ranger_id, reserve_id,animal_id, ranger_id, reserve_id))
        check = cursor.fetchone()
        print("CHECK RESULT:", check)

        if not check:
            raise ValueError("Database query failed")
        if not check["animal_exists"]:
            raise ValueError("Animal not found")
        if not check["ranger_exists"]:
            raise ValueError("Ranger not found")
        if not check["reserve_exists"]:
            raise ValueError("Reserve not found")
        if check["treatment_exists"]:
            raise ValueError("Treatment already exists")
        cursor.execute('INSERT INTO treatments (outcome, animal_id, reserve_id, ranger_id, date) VALUES (%s, %s, %s, %s, %s) RETURNING id',
                       (outcome, animal_id, reserve_id, ranger_id, date))
        treatment_row = cursor.fetchone()
        treatment_id = treatment_row["id"]
        conn.commit()
        return treatment_id
    finally:
        cursor.close()
        conn.close()


def get_ranger_treatments_by_reserve(search_type, search_value):
    if search_type not in ["ranger_id", "ranger_name"]:
        raise ValueError("Search type must be 'ranger_id' or 'ranger_name'")
    if not search_value:
        raise ValueError("Search value is required")
    if search_type == "ranger_id" and not isinstance(search_value, int):
        raise ValueError("Search value must be an integer")
    if search_type == "ranger_name" and not isinstance(search_value, str):
        raise ValueError("Search value must be a string")

    conn = get_connection()
    cursor = conn.cursor()
    try:
        if search_type == "ranger_id":
            s_type = "r2.id"
        elif search_type == "ranger_name":
            s_type = "r2.name"
        else:
            raise ValueError("Invalid search type")

        ranger_check_col = "id" if search_type == "ranger_id" else "name"
        cursor.execute(f"SELECT 1 FROM rangers WHERE {ranger_check_col} = %s", (search_value,))
        if not cursor.fetchone():
            raise ValueError("Ranger not found")

        query = f"""
        SELECT r.name AS reserve_name, COUNT(DISTINCT t.animal_id) AS animals_count
        FROM treatments t
        JOIN reserves r ON r.id = t.reserve_id
        JOIN rangers r2 on t.ranger_id = r2.id
        WHERE {s_type} = %s
        GROUP BY r.id, r.name
        """
        cursor.execute(query, (search_value,))
        treatments = cursor.fetchall()
        return treatments
    finally:
        cursor.close()
        conn.close()
