import sqlite3 as sql

from app.Sportsbook import Sport, Event, Selection
from app.db_helper import *


class DB:
    def __init__(self):
        self.conn = sql.connect('sportsbook.db')
        self.conn.row_factory = sql.Row

    def close_connection(self):
        try:
            self.conn.close()
        except Exception as ex:
            self.conn.close()
            print("Exception occurred while closing the connection:", ex)

    def create_sport_table(self):
        try:
            with self.conn:
                self.conn.execute("""
                CREATE TABLE IF NOT EXISTS SPORT (
                        id INTEGER PRIMARY KEY, 
                        Name TEXT,
                        Slug TEXT,
                        Active TEXT
                );
                """)
        except Exception as ex:
            self.conn.close()
            print("Exception occurred while creating table:", ex)

    def create_event_table(self):
        try:
            with self.conn:
                self.conn.execute("""
                   CREATE TABLE IF NOT EXISTS EVENT (
                           id INTEGER PRIMARY KEY, 
                           Name TEXT,
                           Slug TEXT,
                           Active TEXT,
                           Type TEXT,
                           Sport_id INTEGER,
                           Status TEXT,
                           Scheduled_start TEXT,
                           Actual_start TEXT,
                           FOREIGN KEY(Sport_id) REFERENCES SPORT(id)
                   );
                   """)
        except Exception as ex:
            self.conn.close()
            print("Exception occurred while creating table:", ex)

    def create_selection_table(self):
        try:
            with self.conn:
                self.conn.execute("""
                   CREATE TABLE IF NOT EXISTS SELECTION (
                           id INTEGER PRIMARY KEY, 
                           Name TEXT,
                           Event_id INTEGER,
                           Price REAL,
                           Active TEXT,
                           Outcome TEXT,
                           FOREIGN KEY(Event_id) REFERENCES EVENT(id)
                   );
                   """)
        except Exception as ex:
            self.conn.close()
            print("Exception occurred while creating table:", ex)

    # SPORTS

    def insert_sports(self, sport: Sport):
        try:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO SPORT (id, name, slug, active) VALUES (NULL, ?, ?, ?)",
                        (sport.name, sport.slug, sport.active))
            self.conn.commit()
            return cur.lastrowid
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while inserting in sports:", ex)
            return None

    def update_sports(self, sport: Sport):
        try:
            cur = self.conn.cursor()
            cur.execute("UPDATE SPORT SET name = ?, slug = ?, active = ? WHERE id =?",
                        (sport.name, sport.slug, sport.active, sport.id))

            self.conn.commit()
            return sport.id
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while updating in sport:", ex)
            return None

    def deactivate_sports(self, sport_id):
        try:
            cur = self.conn.cursor()
            cur.execute("UPDATE SPORT SET active = 'FALSE' WHERE id =?", str(sport_id))
            self.conn.commit()
            return sport_id
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while deactivating sport:", ex)
            return None

    def get_filtered_sports(self, filters):
        try:
            query = "SELECT * FROM SPORT sport"
            filter_query = ""
            if filters is not None:
                filter_query = make_sports_filter(filters)
            query += filter_query
            print(query)
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return rows
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while fetching all sports:", ex)
            return None

    # EVENTS
    def insert_event(self, event: Event):
        try:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO EVENT (id, Name, Slug, Active, Type, Sport_id, Status , Scheduled_start, Actual_start) "
                "VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                (event.name, event.slug, event.active, event.type, event.sport_id, event.status, event.scheduled_start,
                 event.actual_start))
            self.conn.commit()
            return cur.lastrowid
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while inserting in event:", ex)
            return None

    def update_event(self, event: Event):
        try:
            cur = self.conn.cursor()
            cur.execute(
                "UPDATE EVENT SET Name = ?, Slug = ?, Active = ?, Type = ?, Sport_id = ?, Status = ?, Scheduled_start "
                "= ?, Actual_start = ? WHERE id =?",
                (event.name, event.slug, event.active, event.type, event.sport_id, event.status, event.scheduled_start,
                 event.actual_start, event.id))

            self.conn.commit()
            return event.id
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while updating in event:", ex)
            return None

    def deactivate_event(self, event_id):
        try:
            cur = self.conn.cursor()
            cur.execute("UPDATE EVENT SET Active = 'FALSE' WHERE id =?", str(event_id))
            self.conn.commit()
            return event_id
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while deactivating event:", ex)
            return None

    def get_filtered_events(self, filters):
        try:
            query = "SELECT * FROM EVENT event"
            filter_query = ""
            if filters is not None:
                filter_query = make_events_filter(filters)
            query += filter_query
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return rows
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while fetching events:", ex)
            return None

    # SELECTIONS

    def insert_selection(self, selection: Selection):
        try:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO SELECTION (id, Name, Event_id, Price, Active, Outcome) VALUES (NULL, ?, ?, ?, ?, ?)",
                (selection.name, selection.event_id, selection.price, selection.active, selection.outcome))
            self.conn.commit()
            return cur.lastrowid
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while inserting in selection:", ex)
            return None

    def update_selection(self, selection: Selection):
        try:
            cur = self.conn.cursor()
            cur.execute("UPDATE SELECTION SET name = ?, Event_id = ?, Price = ?, Active = ?, Outcome = ? WHERE id =?",
                        (selection.name, selection.event_id, selection.price, selection.active, selection.outcome,
                         selection.id))
            self.conn.commit()
            return selection.id
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while updating in selection:", ex)
            return None

    def deactivate_selection(self, selection_id):
        try:
            cur = self.conn.cursor()
            cur.execute("UPDATE SELECTION SET Active = 'FALSE' WHERE id =?", str(selection_id))
            self.conn.commit()
            return selection_id
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while deactivating:", ex)
            return None

    def get_filtered_selections(self, filters):
        try:
            query = "SELECT * FROM SELECTION selection"
            filter_query = ""
            if filters is not None:
                filter_query = make_selections_filter(filters)
            query += filter_query
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return rows
        except Exception as ex:
            self.conn.rollback()
            self.conn.close()
            print("Exception occurred while fetching selections:", ex)
            return None
