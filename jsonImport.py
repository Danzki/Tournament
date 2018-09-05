import json
from backend import Team, Tournament, Transport
import os
import shutil

#JSON import class to import data (team, tournament, match, result)
class jsonFile:
    def __init__(self, jsonpath, jsonfile):
        self.path = jsonpath
        self.file = jsonfile
        path = os.path.join(jsonpath, jsonfile)
        with open(path, 'r') as f:
            strToJson = f.read()
            self.obj = json.loads(strToJson, strict=False)

    def __repr__(self):
        return "jsonFile('{}', '{}')".format(self.path, self.file)

    def __str__(self):
        return 'JSON items {}'.format(self.obj.items())

    @property
    def impType(self):
        if 'Team' in self.obj:
            return 'Team'
        elif 'Tournament' in self.obj:
            return 'Tournament'
        elif 'Match' in self.obj:
            return 'Match'
        elif 'Result' in self.obj:
            return 'Resulf'

    @staticmethod
    def teamImport(self):
        return Team(self.obj.get('Team').get('name'), self.obj.get('Team').get('city'), self.obj.get('Team').get('logo'))

    @staticmethod
    def tournamentImport(self):
        pass

    @staticmethod
    def matchImport(self):
        pass

    @staticmethod
    def resultImport(self):
        pass

    def Import(self):
        self.impType
        if self.impType == 'Team':
            return self.teamImport(self)
        elif self.impType == 'Tournament':
            return self.tournamentImport(self)
        elif self.impType == 'Match':
            return self.matchImport(self)
        elif self.impType == 'Result':
            return self.resultImport(self)


#JSON scanner class to scan IN & OUT Transports
class jsonScanner:
    def __init__(self, path):
        self.path = path

    def scan(self, side, move=True):
        jsonArray = []
        d = Transport()
        for root, dirs, files in os.walk(self.path):
            for f in files:
                if os.path.splitext(f)[1] == '.json':
                    jsonObj = jsonFile(self.path, f)
                    jsonArray.append(jsonObj)
                    if move:
                        shutil.move(os.path.join(self.path, f), os.path.join(side=='IN' ? d.f_in['arch'] : d.f_out['arch'], f))
        return jsonArray
