from main import conn, cursor

def query_request(query, type="GET"):
    if type == "GET":
        cursor.execute(query)
        data = cursor.fetchall()
        return data

def nicknames(uuid):
    cursor.execute("SELECT * FROM plan_nicknames WHERE uuid=%s", (uuid,))
    data  = cursor.fetchall()
    dData = {}
    lData = []
    for registro in data:
        dData = {"name":registro[2],"last_used":registro[4]}
        lData.append(dData)
    return lData
