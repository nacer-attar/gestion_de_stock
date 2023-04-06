class produit :
    def __init__(self,conn) -> None:
        self.conn = conn
        self.cursor = conn.cursor()