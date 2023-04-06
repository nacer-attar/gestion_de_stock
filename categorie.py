class categorie:
    def __init__(self,conn) -> None:
        self.conn = conn
        self.cursor = conn.cursor()

    def addcat(self):
        request = "INSERT INTO "