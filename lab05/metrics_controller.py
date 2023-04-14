from connection import Database
from metric import Metric
from measurement_enum import MeasurementEnum
import config


class MetricsController:

    def __init__(self) -> None:
        self.db = Database(db=config.DBNAME, password=config.DB_PASSWORD)

    def sql_builder(self, measurement_enum: MeasurementEnum, date_from: str | None, date_to: str | None) -> str:
        sql = f"SELECT {measurement_enum.value}, time FROM data "

        if date_from:
            sql += f"WHERE time < {date_from} "

        if date_to:
            if "WHERE" not in sql:
                sql += f"WHERE "
            else:
                sql += "and "

            sql += "time > {date_from}"

        return sql

    def get_metric(self, measurement_enum: MeasurementEnum, date_from: str | None = None, date_to: str | None = None) -> Metric:
        sql = self.sql_builder(measurement_enum, date_from, date_to)
        result = self.db.fetch(sql)

        x = []
        y = []

        for result, time in result:
            x.append(result)
            y.append(time)

        return Metric(x, y)
