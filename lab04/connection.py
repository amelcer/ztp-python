
import pymysql
from pymysql import Connection as MysqlConn


class Database:

    def __init__(self, db: str | None = None, host: str = "localhost", user: str = "root", password: str = "") -> None:
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connect(self) -> MysqlConn:
        return pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.db)

    def exec(self, sql: str) -> bool:
        ok = False
        connection = None
        current = None
        try:
            connection = self.connect()
            current = connection.cursor()
            current.execute(sql)
            connection.commit()
            ok = True
        except pymysql.connect.Error as error:
            ("DB Error: {}".format(error))
        except Exception as e:
            print(e)
        finally:
            if connection:
                if current:
                    current.close()
                connection.close()
        return ok
