import settings
import rethinkdb as r
import time

#call right when people are starting (opening the level editor/leaving main menu)
def startGame():
    if settings.ip == "localhost":
        conn = r.connect(settings.ip, int(settings.port))
        if r.table_list().count('levels').run(conn) == 1:
            r.table_drop('levels').run(conn)
            r.table_drop('users').run(conn)

        r.table_create('levels').run(conn)
        r.table_create('users').run(conn)

        r.table('users').insert({'username' : settings.user, 'time' : 999, 'done': False, 'type' : 'player', 'pos' : (0,0)}).run(conn)
        r.table('users').insert({'numUsers' : 1 , 'type' : 'numUsers'}).run(conn)

    else:
        conn = r.connect(settings.ip, int(settings.port))
        r.table('users').insert({'username' : settings.user, 'time' : 999, 'done': False, 'type' : 'player', 'pos' : (0,0)}).run(conn)
        r.table('users').filter({'type':'numUsers'}).update({'numUsers' : r.row['numUsers']+1}).run(conn)

#called when level is finished building, should force the players to wait, takes in an array that is the level
def levelBuilt(levelArray):
    conn = r.connect(settings.ip, int(settings.port))
    r.table('levels').insert({'level' : levelArray, 'type' : 'level' }).run(conn)

    waiting = True
        
    while waiting:
        numPlayersCursor = r.table('users').filter({'type' : 'numUsers'}).run(conn)
        numPlayersList = list(numPlayersCursor)
        numPlayers = numPlayersList[0]['numUsers']
        numFinishedCursor = r.table('levels').filter({'type' : 'level'}).run(conn)
        numFinishedList = list(numFinishedCursor)
        numFinished = len(numFinishedList)
        if numPlayers == numFinished:
            waiting = False
            #we move onto the game
        else:
            time.sleep(1)

#returns an array of levels (each level is of course its own array)
def getLevels():
    conn = r.connect(settings.ip, int(settings.port))
    levelsCursor = r.table('levels').run(conn)
    Levels = []
    for level in levelsCursor:
        tiles = level['level']
        Levels.append(tiles)
        #ok now you have the tiles of the level
    return Levels


#returns list of positions as tuples, takes in our players position as a tuple (x,y)
def updatePlayerPositions(playerPosition):
    conn = r.connect(settings.ip, int(settings.port))
    r.table('users').filter({'username' : settings.user}).update({'pos' : playerPosition}).run(conn)

    usersCursor = r.table('users').filter({'type':'player'}).run(conn)
    positions = []
    for user in usersCursor:
        if(user['username'] == settings.user:
           pass
        else:
            positions.append(user['pos'])
        #This is the position of every user as a tuple (x,y)
    return positions

#called when the player finishes the round, takes in his time to finish and returns the winner of the round
def roundFinished(timeToFinish):
    conn = r.connect(settings.ip, int(settings.port))
    r.table('users').filter({'username' : settings.user}).update({'time': timeToFinish}).run(conn)
    r.table('users').filter({'username' : settings.user}).update({'done': True}).run(conn)

    waiting = True

    while waiting:
        numPlayersCursor = r.table('users').filter({'type' : 'numUsers'}).run(conn)
        numPlayersList = list(numPlayersCursor)
        numPlayers = numPlayersList[0]['numUsers']
        numFinishedCursor = r.table('users').filter({'done' : True}).run(conn)
        numFinishedList = list(numFinishedCursor)
        numFinished = len(numFinishedList)
        if numPlayers == numFinished:
            players = r.table('users').filter({'type' : 'player'}).run(conn)
            fastest = 99999
            for document in players:
                if document['time'] < fastest:
                    fastest = document['time']
                    winner = document['username']
                else:
                    pass
        else:
            time.sleep(1)
        waiting = False
           
    return winner



            
