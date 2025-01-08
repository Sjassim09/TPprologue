# JassimPrologTp
TP Prolog de Sirat Jassim
Je vais répondre aux question ici :

Exo1 :
1 Qui est le père de Marc ?
- Jacques

2 Marc a-t-il des enfants ?
- Oui Sophie


Exercice 2: 
    1. Qui est le grand-parent de Paul ?
      Il n'a pas de grand parent
      grandparent(X,paul). 
      false
       
   2. Jacques est-il grand-parent de Sophie ?
    Oui il est le grand parent


Exercice 3 :
1. Paul a-t-il des frères ou des sœurs ?
   Non il n'a pas de frère ou de soeur
    freres(X,Y) :- parent(Z,X), parent(Z,Y).


Exercice 4 :
1. Trouvez tous les hommes dans la base de données :
 findall(X, homme(X), Liste).
Liste = [pierre, marc, paul, jacques].

2.Recherchez tous les parents de Sophie :
findall(X, parent(X,sophie), Liste).
Liste = [marc].


EXERCICE 8 :
    1. Marc est-il l'oncle de Paul ?
    Non car ils ne sont pas lié vus qu'on ne sait pas qui est le pere de pierre, et il faudrait que pierre et marc soient  frère donc avec le même père
    oncle(marc,paul).
    false.

  2. Quels sont les oncles de Sophie ?
      oncle(X,sophie).
      X = marc

Exercice 8 :
1. Interrogez la base de connaissances pour trouver les cousins de Paul :
 cousin(X,paul).
false.
