#for this game to work it is assumed that someone has a rethinkdb server running and that people are on the same network (hamachi should work) import settings. Server should be started with --bind all.
import rethinkdb as r
import time
import settings

#call right when people are starting (opening the level editor/leaving main menu)
def startGame():
    if settings.connectionSettings['ip'] == "localhost":
        conn = r.connect(settings.connectionSettings['ip'], int(settings.connectionSettings['port']))
        if len(r.table_list().run(conn)) == 0:
            r.table_create('levels').run(conn)
            r.table_create('users').run(conn)
            
        if r.table('levels').count().run(conn) > 0:
            r.table('levels').delete().run(conn)
            r.table('users').delete().run(conn)

        r.table('users').insert({'username' : settings.connectionSettings['user'], 'time' : 999, 'done': False, 'type' : 'player', 'pos' : (0,0)}).run(conn)
        r.table('users').insert({'numUsers' : 1 , 'type' : 'numUsers'}).run(conn)

    else:
        conn = r.connect(settings.connectionSettings['ip'], int(settings.connectionSettings['port']))

        if len(r.table_list().run(conn)) != 0: #firstly, check if there are tables on the db
            if r.table('users').filter({'done': True}).count().run(conn) > 0: #if this is true surely we are looking at old data
                for changes in r.table('users').filter({'done': True}).changes().run(conn): #post up here to check for changes
                    break #if anything changes than our stuff is updated (almost definitely)
            
        r.table('users').insert({'username' : settings.connectionSettings['user'], 'time' : 999, 'done': False, 'type' : 'player', 'pos' : (0,0)}).run(conn)
        r.table('users').filter({'type':'numUsers'}).update({'numUsers' : r.row['numUsers']+1}).run(conn)

#called when level is finished building, should force the players to wait, takes in an array that is the level
def levelBuilt(levelArray):
    conn = r.connect(settings.connectionSettings['ip'], int(settings.connectionSettings['port']))
    r.table('levels').insert({'level' : levelArray, 'type' : 'level' }).run(conn)

    waiting = True
        
    while waiting:
        numPlayersCursor = r.table('users').filter({'type' : 'numUsers'}).run(conn)
        numPlayersList = list(numPlayersCursor)
        numPlayers = numPlayersList[0]['numUsers']
        print numPlayers
        numFinishedCursor = r.table('levels').filter({'type' : 'level'}).run(conn)
        numFinishedList = list(numFinishedCursor)
        numFinished = len(numFinishedList)
        print numFinished
        if numPlayers == numFinished:
            waiting = False
            #we move onto the game
        else:
            time.sleep(1)

#returns an array of levels (each level is of course its own array)
def getLevels():
    conn = r.connect(settings.connectionSettings['ip'], int(settings.connectionSettings['port']))
    levelsCursor = r.table('levels').run(conn)
    Levels = []
    for level in levelsCursor:
        tiles = level['level']
        Levels.append(tiles)
        #ok now you have the tiles of the level
    return Levels


#returns list of positions as tuples, takes in our players position as a tuple (x,y)
def updatePlayerPositions(playerPosition):
    conn = r.connect(settings.connectionSettings['ip'], int(settings.connectionSettings['port']))
    r.table('users').filter({'username' : settings.connectionSettings['user']}).update({'pos' : playerPosition}).run(conn)

    usersCursor = r.table('users').filter({'type':'player'}).run(conn)
    positions = []
    for user in usersCursor:
        if(user['username'] == settings.connectionSettings['user']):
           pass
        else:
            positions.append(user['pos'])
        #This is the position of every user as a tuple (x,y)
    return positions

#called when the player finishes the round, takes in his time to finish and returns the winner of the round
def roundFinished(timeToFinish):
    conn = r.connect(settings.connectionSettings['ip'], int(settings.connectionSettings['port']))
    r.table('users').filter({'username' : settings.connectionSettings['user']}).update({'time': timeToFinish}).run(conn)
    r.table('users').filter({'username' : settings.connectionSettings['user']}).update({'done': True}).run(conn)


    while True:
        numPlayersCursor = r.table('users').filter({'type' : 'numUsers'}).run(conn)
        numPlayersList = list(numPlayersCursor)
        numPlayers = numPlayersList[0]['numUsers']
        numFinishedCursor = r.table('users').filter({'done' : True}).run(conn)
        numFinishedList = list(numFinishedCursor)
        numFinished = len(numFinishedList)
        if numPlayers == numFinished:
            players = r.table('users').filter({'type' : 'player'}).sort(index='time').run(conn)
            playersList = list(players)
            return playersList
#           for document in players:
#               if document['time'] < fastest:
#                    fastest = document['time']
#                    winner = document['username']
#            return winner
        else:
            time.sleep(1)


#if the same crew of people want to play again call this, and then jump into the level editor
def restartGame():
    if settings.connectionSettings['ip'] == "localhost":
        conn = r.connect(settings.connectionSettings['ip'], int(settings.connectionSettings['port']))
        r.table('levels').delete().run(conn)

        r.table('users').filter({'type' : 'player'}).update({'time' : 999}).run(conn)
        r.table('users').filter({'type' : 'player'}).update({'done' : False}).run(conn)
    else:
        conn = r.connect(settings.connectionSettings['ip'], int(settings.connectionSettings['port']))

        if len(r.table_list().run(conn)) != 0: #firstly, check if there are tables on the db
            if r.table('users').filter({'done': True}).count().run(conn) > 0: #if this is true surely we are looking at old data
                for changes in r.table('users').filter({'done': True}).changes().run(conn): #post up here to check for changes
                    break #if anything changes than our stuff is updated (almost definitely)

        #nothing actually happens for the clients here, they should just be held up until the host has reset the game. Upon which they go back into the level editor and things continue

            
