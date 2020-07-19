from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
engine = create_engine("postgresql://riyad123:RiyadDatabase1@localhost:5432/mydatabase")
db = scoped_session(sessionmaker(bind=engine))
def main():
    flightid= int(input("Flight ID:"))
    flight= db.execute("SELECT * FROM flights WHERE id= :id",
        {"id":flightid}).fetchone()
    if flight == NONE:
        print(f"No existing flight with id {flightid}")
        return
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id= :flight_id",
    {"flight_id":flightid}).fetchall()
    print("\passengers")
    for passenger in passengers:
        print(f"Passenger: {name}")
    if len(passengers)==0:
        print(f"No passengers with flight ID: {flightid}")
if __name__=="__main__":
    main()
