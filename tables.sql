create table Team (
    TeamId INTEGER PRIMARY KEY UNIQUE NOT NULL,
    Name VARCHAR NOT NULL,
    City VARCHAR,
    Logo VARCHAR
);


create table Tournament (
    TornamentId INTEGER PRIMARY KEY UNIQUE NOT NULL,
    Name VARCHAR NOT NULL,
    Matches INTEGER,
    Teams INTEGER,
    Setting INTEGER
);

create table Setting (
    Setting INTEGER PRIMARY KEY UNIQUE NOT NULL,
    TournamentId INTEGER,
    Teams INTEGER,
    Groups INTEGER,
    Rounds INTEGER,
    PlayOff INTEGER,
    PlayOffRound INTEGER,
    PlayOffMatch INTEGER
);

create table Match (
    MatchId INTEGER PRIMARY KEY UNIQUE NOT NULL,
    TeamHome INTEGER,
    TeamGuest INTEGER,
    GoalHome INTEGER,
    GoalGuest INTEGER,
    TournamentId INTEGER
);

create table Schedule (
    ScheduleId INTEGER PRIMARY KEY UNIQUE NOT NULL,
    MatchId INTEGER,
    MatchDate DATE
);
