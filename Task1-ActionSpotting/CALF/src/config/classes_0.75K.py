import torch


# Event name to label index fororor SoccerNet-V2
EVENT_DICTIONARY_V2 = {"Penalty":0,"Kick-off":1,"Goal":2,"Substitution":3,"Offside":4,"Shots on target":5,
                                "Shots off target":6,"Clearance":7,"Ball out of play":8,"Throw-in":9,"Foul":10,
                                "Indirect free-kick":11,"Direct free-kick":12,"Corner":13,"Yellow card":14
                                ,"Red card":15,"Yellow->red card":16}

INVERSE_EVENT_DICTIONARY_V2 = {0:"Penalty",1:"Kick-off",2:"Goal",3:"Substitution",4:"Offside",5:"Shots on target",
                                6:"Shots off target",7:"Clearance",8:"Ball out of play",9:"Throw-in",10:"Foul",
                                11:"Indirect free-kick",12:"Direct free-kick",13:"Corner",14:"Yellow card"
                                ,15:"Red card",16:"Yellow->red card"}

# Values of the K parameters (in seconds) in the context-aware loss
K_V2 = torch.FloatTensor([[-75, -73, -15, -30, -72, -3, -6, -69, -74, -23, -56, -7, -72, -56, -15, -63, -13],
                          [-37, -36, -7, -15, -36, -2, -3, -34, -37, -11, -27, -3, -36, -28, -7, -31, -6],
                          [37, 36, 45, 7, 36, 2, 3, 34, 37, 11, 27, 3, 36, 28, 7, 31, 6],
                          [75, 73, 67, 15, 72, 3, 6, 69, 74, 23, 56, 7, 72, 56, 15, 63, 13]]).cuda()
