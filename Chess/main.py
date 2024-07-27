from chess import Chess;

ch = Chess("mann","meet");
ch.load()
# ch.show();


while True:
    ch.show()
    fom = input("piece from: ")
    ch.checkMoves(fom)
    to = input("piece to: ")
    ch.move(fom,to)