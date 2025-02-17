homme(pierre).
homme(marc).
homme(paul).
homme(jacques).
femme(marie).
femme(sophie).
femme(julie).

parent(pierre, paul).
parent(marie, paul).
parent(marc, sophie).
parent(jacques, marc).
parent(julie, sophie).

p�re(X, Y) :- homme(X), parent(X, Y).
m�re(X, Y) :- femme(X), parent(X, Y).

grandparent(X,Y) :- parent(X,Z), parent(Z,Y).

frereSoeur(X,Y) :- parent(Z,X), parent(Z,Y).

longueur([],0).
longueur([_ | Queue], N) :- longueur(Queue, M), N is M +1.

membre(X, [X|_]).
membre(X, [_|T]) :- membre(X, T).

oncle(X, Y) :- homme(X), parent(Z, Y), frereSoeur(X, Z).
tante(X, Y) :- femme(X), parent(Z, Y), frereSoeur(X, Z).

cousin(X,Y) :- parent(Z,X), frereSoeur(Z,W),parent(W,Y).
