import pypyodbc as odbc

class conexionDB:
    def __init__(self):    
        self.DRIVER_NAME = 'SQL SERVER'
        self.SERVER_NAME = 'Laptop_Sandox'
        self.DATABASE_NAME = 'BIBLIOTECA'

        self.connection_string = f""" 
            DRIVER={{{self.DRIVER_NAME}}};
            SERVER={self.SERVER_NAME};
            DATABASE={self.DATABASE_NAME};
            Trust_Connection=yes;
        """

        self.conn = odbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()