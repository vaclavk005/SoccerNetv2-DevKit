import torch

# 8 classes
# # Event name to label index fororor SoccerNet-V2
# EVENT_DICTIONARY_V2 = {"Penalty":0,"Goal":1,"Clearance":2,"Ball out of play":3,
#                        "Throw-in":4,"Foul":5,"Direct free-kick":6,"Corner":7}

# INVERSE_EVENT_DICTIONARY_V2 = {0:"Penalty",1:"Goal",2:"Clearance",3:"Ball out of play",
#                                4:"Throw-in",5:"Foul",6:"Direct free-kick",7:"Corner"}

# K_V2 = torch.FloatTensor([[-40, -8, -37, -39, -12, -30, -38, -30],
#                           [-20, -4, -18, -20, -6, -14, -19, -15],
#                           [20, 10, 18, 20, 6, 14, 19, 15],
#                           [40, 20, 37, 39, 12, 30, 38, 30]]).cuda()

# 17 classes
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
K_V2 = torch.FloatTensor([[-100, -98, -20, -40, -96, -5, -8, -93, -99, -31, -75, -10, -97, -75, -20, -84, -18],
                          [-50, -49, -10, -20, -48, -3, -4, -46, -50, -15, -37, -5, -49, -38, -10, -42, -9],
                          [50, 49, 60, 10, 48, 3, 4, 46, 50, 15, 37, 5, 49, 38, 10, 42, 9],
                          [100, 98, 90, 20, 96, 5, 8, 93, 99, 31, 75, 10, 97, 75, 20, 84, 18]]).cuda()

# K_V2 = torch.FloatTensor([[-40, -39, -8, -16, -38, -5, -5, -37, -39, -12, -30, -4, -38, -30, -8, -33, -7],
#                           [-20, -19, -4, -8, -19, -3, -3, -18, -20, -6, -14, -2, -19, -15, -4, -16, -3],
#                           [20, 19, 24, 4, 19, 3, 3, 18, 20, 6, 14, 2, 19, 15, 4, 16, 3],
#                           [40, 39, 36, 8, 38, 5, 5, 37, 39, 12, 30, 4, 38, 30, 8, 33, 7]]).cuda()