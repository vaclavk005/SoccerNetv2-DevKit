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
K_V2 = torch.FloatTensor([[-50, -49, -10, -20, -48, -2, -4, -46, -49, -15, -37, -5, -48, -37, -10, -42, -9],
                          [-25, -24, -5, -10, -24, -1, -2, -23, -25, -7, -18, -2, -24, -19, -5, -21, -4],
                          [25, 24, 30, 5, 24, 1, 2, 23, 25, 7, 18, 2, 24, 19, 5, 21, 4],
                          [50, 49, 45, 10, 48, 2, 4, 46, 49, 15, 37, 5, 48, 37, 10, 42, 9]]).cuda()
