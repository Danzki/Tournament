from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from jsonImport import jsonFile, jsonScanner
import os
from backend import Team, Tournament, Transport

if __name__ == "__main__":
    DB = create_engine(r'sqlite:///DB/TourDB.DB', echo=False)

    #create a session
    Session = sessionmaker(bind=DB)
    session = Session()

    d = Transport()
    scanIN = jsonScanner(d.f_in['in'])
    array = scanIN.scan('IN')

    for j in array:
        team_to_imp = j.Import()
        print(team_to_imp)
        team_to_imp.insert(session)

    #team_1 = jObj.Import()
    #team_2 = Team('Inter', 'Milan')

    # team_1.insert(session)
    # team_2.insert(session)

    # print('Print data from DB table Team:')
    # ret = session.query(TeamTable).all()
    # for item in ret:
    #    print('teamId={}, name={}, city={}, logo={}'.format(item.teamId, item.name, item.city, item.logo))
