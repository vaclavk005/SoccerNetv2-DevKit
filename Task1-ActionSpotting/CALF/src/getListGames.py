from SoccerNet.Downloader import getListGames as getGames

def getListGames(split):
    matches = ["krajsky_prebor/kosutka_zruc","krajsky_prebor/petrinb_kosutka","krajsky_prebor/robstav_vltavin",
               "krajsky_prebor/hostoun_admira","krajsky_prebor/slaviab_bohemiansb"]
    if split == "train":
        list = getGames(split)
        list = list[:2]+list[-3:]
        list.extend(matches)
        return list
    if split == "valid":
        list = getGames(split)
        list = list[:3]+list[-4:-2]
        list.extend(matches)
        return list
    if split == "test":
        list = getGames(split)
        list.extend(matches)
        return matches
    # return ["england_epl/2014-2015/2015-05-17 - 18-00 Manchester United 1 - 1 Arsenal"]
    # return ["krajsky_prebor/kosutka_zruc"]