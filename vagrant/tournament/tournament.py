#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname=tournament")
        cur = db.cursor()
        return db, cur
    except:
        print "Unable to connect to the database."


def deleteMatches():
    """Remove all the match records from the database."""
    
    db, cur = connect()
    cur.execute("DELETE FROM matches")
    db.commit()
    cur.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cur = connect()
    cur.execute("DELETE FROM players") 
    db.commit()
    cur.close() 

def countPlayers():
    """Returns the number of players currently registered."""
    db, cur = connect()
    cur.execute("SELECT COUNT(name) FROM players")
    count = cur.fetchone()
    cur.close() 
    return count[0]    
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db, cur = connect()
    cur.execute("INSERT INTO players (name) VALUES (%s)", [name])
    db.commit()
    cur.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cur = connect()
    cur.execute("SELECT * FROM standings")
    standings_list = cur.fetchall()
    cur.close() 
    return standings_list



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cur = connect()
    cur.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)", [winner, loser])
    db.commit()
    cur.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    players = int(countPlayers())

    pairs = []
    if players % 2 == 0 and players > 0:
        for p in range(players):
            if p % 2 == 0:
                id1 = standings[p][0]
                name1 = standings[p][1]
            
                id2 = standings[p+1][0]
                name2 = standings[p+1][1]
                
                pair = (id1, name1, id2, name2)
                pairs.append(pair)

    return pairs
    



