import queue

Complete=[0,1,2,
          3,4,5,
          6,7,8]
Given=[3,1,2,0,4,5,6,7,8]

def Start():
    bfs(Given)

def FindZero(Table):
    index=0
    for number in Table:
        return index
        index+=1

def FindNeighbour(Zero):
    switch={0:[3,1],
            1:[4,0,2],
            2:[5,1],
            3:[0,6,4],
            4:[1,7,3,5],
            5:[2,8,4],
            6:[3,7],
            7:[4,6,8],
            8:[5,7]}
    return switch[Zero]

def MoveZero(Table,Zero,Neighbour):
    Temp=Table[Neighbour]
    Table[Neighbour]=0
    Table[Zero]=Temp
    return Table

def bfs(Root):
    S={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    Q=queue.Queue()

    S[FindZero(Root)].append(Root)
    Q.put(Root)

    while(Q.empty!=True):
        Current=Q.get()
        if(Current==Complete):
            return Current
        Zero=FindZero(Current)
        Neighbours=FindNeighbour(Zero)
        for Neighbour in Neighbours:
            New=MoveZero(Current,Zero,Neighbour)
            if New not in S[Neighbour]:
                S[Neighbour].append(New)
                print(S)

Start()