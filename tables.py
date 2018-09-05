from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine(r'sqlite:///DB\TourDB.DB')
Base = declarative_base()

#Class Team
#linked to table Team\
#Store data about teams
class TeamTable(Base):
    __tablename__ = 'Team'
    teamId = Column(Integer, primary_key=True)
    name = Column(String(300))
    city = Column(String(300))
    logo = Column(String(4000))

    def __init__(self, name, city, logo):
        self.name = name
        self.city = city
        self.logo = logo

    def __repr__(self):
        return "TeamTable('{}, {}, {}')".format(self.name, self.city, self.logo)


#Class Tournament
#linked to Tournament table
#Store data about tornaments
class TournamentTable(Base):
    __tablename__ = 'Tournament'
    TournamentId = Column(Integer, primary_key=True)
    Name = Column(String(300))
    Matches = Column(Integer)
    Teams = Column(Integer)
    Setting = Column(Integer)

    def __init__(self, Name, IntName, Matches=None, Teams=None, Setting=None):
        self.name = Name
        self.intname = IntName
        self.matches = Matches
        self.teams = Teams
        if Setting is None:
            self.setting = []
        else:
            self.setting = Setting

    def __repr__(self):
        return "Tournament('{}', '{}', None, None, None)".format(self.name, self.IntName)

    def __str__(self):
        return "<Tornament('{}', '{}', '{}')>" % (self.name, self.intname, self.matches, self.teams, self.setting)

#Class Setting
#linked to Setting table
#Store data for tournament settings
class SettingTable(Base):
    __tablename__ = 'Setting'
    SettingId = Column(Integer, primary_key=True)
    Name = Column(String(500))
    TournamentId = Column(Integer)
    TeamQuantity  = Column(Integer)
    GroupQuantity  = Column(Integer)
    RoundMactchQuantity  = Column(Integer)
    RoundQuantity  = Column(Integer)

    def __init__(self, Name, TournamentId, TeamQuantity, GroupQuantity, RoundMactchQuantity, RoundQuantity):
        self.name = Name
        self.tournamentId = TournamentId
        self.TeamQuantity = TeamQuantity
        self.GroupQuantity = GroupQuantity
        self.RoundMactchQuantity = RoundMactchQuantity
        self.RoundQuantity = RoundQuantity

    def __repr__(self):
        return "<Setting('%s','%s', '%s')>" % (self.name, self.tournamentId, self.TeamQuantity, self.GroupQuantity, self.RoundQuantity, self.RoundMactchQuantity)

#Class Match
#linked to table Match
#Store data about matches
class MatchTable(Base):
    __tablename__ = 'Match'
    MatchId = Column(Integer, primary_key=True)
    TeamHomeId = Column(Integer)
    TeamGuestId = Column(Integer)
    GoalHome = Column(Integer)
    GoalGuest = Column(Integer)
    TournamentId = Column(Integer)

    def __init__(self, TeamHomeId, TeamGuestId, GoalHome, GoalGuest, TournamentId):
        self.teamHomeId = TeamHomeId
        self.teamGuestId = TeamGuestId
        self.goalHome = GoalHome
        self.goalGuest = GoalGuest
        self.tournamentId = TournamentId

    def __repr__(self):
        return "<Match('%s','%s', '%s')>" % (self.teamHomeId, self.teamGuestId, self.goalHome, self.goalGuest, self.tournamentId)

#Class Schedule
#linked to table Schedule
#Store data about matches schedules
class ScheduleTable(Base):
    __tablename__ = 'Schedule'
    ScheduleId = Column(Integer, primary_key=True)
    MatchId = Column(Integer)
    MatchDate = Column(Date)

    def __init__(self, MatchId, MatchDate):
        self.matchId = MatchId
        self.matchDate = MatchDate

    def __repr__(self):
        return "<Match Schedule('%s','%s', '%s')>" % (self.matchId, self.matchDate)
