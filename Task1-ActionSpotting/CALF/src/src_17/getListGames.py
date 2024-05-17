import json
import os
from SoccerNet.Downloader import getListGames as getGames

def getListGames(split):

    dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(dir, 'json', 'matches.json')

    with open(json_path, 'r') as f:
        matches_data = json.load(f)

        train_matches = matches_data['train_matches']
        valid_matches = matches_data['valid_matches']
        test_matches = matches_data['test_matches']

    if split == "train":
        # list = getGames(split)
        # # list = list[0:5] + list[-5:] # 10 SoccerNet
        # list = list[:50] + list[-50:] # 100 SoccerNet
        # list.extend(train_matches)
        # return list  # 10/100 SoccerNet + 8 own
        return train_matches # 8 own
    
    if split == "valid":
        # list = getGames(split)
        # list = list[10:13]+list[-4:-2]
        # list.extend(valid_matches)
        return valid_matches
    
    if split == "test":
        return test_matches