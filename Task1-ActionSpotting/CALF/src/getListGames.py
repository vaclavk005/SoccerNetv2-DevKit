from SoccerNet.Downloader import getListGames as getGames

def getListGames(split):
    train_matches = ["krajsky_prebor/kosutka_zruc", "krajsky_prebor/cheb_hrebec",
                     "krajsky_prebor/kosutka_stribro","krajsky_prebor/robstav_vltavin",
                     "krajsky_prebor/kosutka_myto", "krajsky_prebor/benesov_spoje",
                     "krajsky_prebor/slaviab_bohemiansb", "krajsky_prebor/klatovy_kosutka"]
    
    valid_matches = ["krajsky_prebor/petrinb_kosutka","krajsky_prebor/hostoun_admira"]

    test_matches = ["krajsky_prebor/petrinb_kosutka","krajsky_prebor/hostoun_admira"]

    if split == "train":
        list = getGames(split)
        list = list[0:5] + list[-5:] # 10 SoccerNet
        # list = list[:50] + list[-50:] # 100 SoccerNet
        list.extend(train_matches)
        return list  # 10/100 SoccerNet + 8 own
        # return train_matches # 8 own
    
    if split == "valid":
        list = getGames(split)
        list = list[10:13]+list[-4:-2]
        list.extend(valid_matches)
        return list
    
    if split == "test":
        return test_matches