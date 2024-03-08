from SoccerNet.Downloader import getListGames as getGames
# from dataset import SoccerNetClips

list1 = getGames("train")
list2 = getGames("valid")
list3 = getGames("test")
kraj = ["krajsky_prebor/kosutka_zruc","krajsky_prebor/petrinb_kosutka","krajsky_prebor/robstav_vltavin"]
# list.extend(kraj)

print(list1)
print(len(list1))

print(list2)
print(len(list2))

print(list3)
print(len(list3))

# dataset_Train = SoccerNetClips(path=args.SoccerNet_path, features=args.features, split="train", framerate=args.framerate, chunk_size=args.chunk_size*args.framerate, receptive_field=args.receptive_field*args.framerate, chunks_per_epoch=args.chunks_per_epoch)
# print(dataset_Train)
