
import pymysql
from pymysql import Connection as MysqlConn


class Database:

    def __init__(self, db: str = "", host: str = "localhost", user: str = "root", password: str = "") -> None:
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
            result = current.execute(sql)
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

    def fetch(self, sql: str) -> list:
        connection = None
        current = None
        result = None
        try:
            connection = self.connect()
            current = connection.cursor()
            current.execute(sql)
            result = current.fetchall()
        except pymysql.connect.Error as error:
            ("DB Error: {}".format(error))
        except Exception as e:
            print(e)
        finally:
            if connection:
                if current:
                    current.close()
                connection.close()

        return result  # type: ignore
