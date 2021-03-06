-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players ( id SERIAL PRIMARY KEY,
					name TEXT
					);

CREATE TABLE matches (match_id SERIAL PRIMARY KEY,
						winner INT REFERENCES players(id),
						loser INT REFERENCES players(id)
						);

CREATE VIEW standings AS
	SELECT id, name, 
	(SELECT COUNT(winner) 
		FROM matches 
		WHERE winner = id) 
	as wins,
	(SELECT count(match_id) 
		FROM matches 
		WHERE winner = id OR loser = id) 
	as matches
	FROM players 
	ORDER BY wins, matches
