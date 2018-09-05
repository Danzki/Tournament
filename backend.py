from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import TeamTable, TournamentTable
import config as cfg
import os

#Transport class - handle with Config.py folders
class Transport:
    def __init__(self):
        self.source = cfg.json_source
        self.f_in = {'in': os.path.join(os.path.abspath(cfg.json_root), cfg.json_in), 'arch': os.path.join(os.path.abspath(cfg.json_root), cfg.json_arch_in)}
        self.f_out = {'out': os.path.join(os.path.abspath(cfg.json_root), cfg.json_out), 'arch': os.path.join(os.path.abspath(cfg.json_root), cfg.json_arch_out)}
        self.f_error = {'error': os.path.join(os.path.abspath(cfg.json_root), cfg.json_error)}

    def __repr__(self):
        return 'In: {}, Arch_In: {}, Out: {}, Arch_Out: {}, Error: {}'.format(self.f_in['in'], self.f_in['arch'], self.f_out['out'], self.f_out['arch'], self.f_error['error'])

#Team class - object
class Team:
    def __init__(self, name, city, logo=None):
        self.name = name
        self.city = city
        self.logo = logo
        #teamId will be assigned after inserting to DB
        self.teamId = None

    def __repr__(self):
        return "Team('{}', '{}', {})".format(self.name, self.city, self.logo)

    def __str__(self):
        return "Team: '{}' from '{}' with logo in '{}'".format(self.name, self.city, self.logo)

    @property
    def teamId(self):
        return self.__teamId

    @teamId.setter
    def teamId(self, value):
        self.__teamId = value

    #Function for work with DataBase
    def insert(self, session):
         #create a team with check existing
        ret = session.query(TeamTable).filter(TeamTable.name==self.name and TeamTable.city==self.city).first()
        if ret is None:
            db_team_1 = TeamTable(self.name, self.city, self.logo)
            # Add the record to the session object
            session.add(db_team_1)
            # commit the record the database
            session.commit()

        #fill teamId for Instance anyway
        team_id = self.getIdByNameCity(session)
        self.teamId = team_id


    def delete(self, session):
        if self.teamId is not None:
            res = session.query(TeamTable).filter(TeamTable.teamId==self.teamId).delete()

    def update(self, session):
        if self.teamId is not None:
            res = session.query(TeamTable).filter(TeamTable.teamId==self.teamId).first()
            res.name = self.name
            res.city = self.city
            res.logo = self.logo
            session.commit()

    def getIdByNameCity(self, session):
        ret = session.query(TeamTable).filter(TeamTable.name==self.name and TeamTable.city==self.city).first()
        return ret.teamId

    #Info Fucntion
    def getTornaments(self):
        pass

    def winNumber(self, tournament):
        pass

    def drawNumber(self, tournament):
        pass

    def lostNumber(self, tournament):
        pass

#Class Tournament
class Tournament:
    def __init__(self, name, autoschedule=False, matches=None, teams=None, Setting=None):
        self.tournamentId = None
        self.name = name
        self.autoschedule = autoschedule
        if matches is not None:
            self.matches = matches
        if teams is not None:
            self.teams = teams
        if setting is not None:
            self.setting = setting

    def __repr__(self):
        return "Tournament('{}', '{}', '{}', None, None, None)".format(self.name, self.intname, self.autoschedule)

    def __str(self):
        return "Tournament: {} / {}".format(self.name, self.intname)

    #Function for work with DataBase
    def insert(self, session):
        pass

    def delete(self, session):
        pass

    def update(self, session):
        pass
