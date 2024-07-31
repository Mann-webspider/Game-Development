from chess import Chess;

ch = Chess("mann","meet");
ch.load()
# ch.show();


while True:
    ch.show()
    fom = input("Enter Move From: ")
    ch.checkMoves(fom)
    to = input("To: ")
    ch.move(fom,to)