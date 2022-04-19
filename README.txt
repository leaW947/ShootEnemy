--------Introduction-----------

J'ai réalisé un mini-shooter avec le langage Python et le framework Pygame. J'ai
programmé ce jeu avec l'IDE Pycharm. Pour les graphismes de jeu, je les ai fait
moi-même avec PixelEdit principalement.


---------------Déroulement du jeu----------------

Quand on lance le projet, on arrive directement sur l'écran de jeu.

Nous incarnons le sprite vert situé à gauche de l'écran. On peut le déplacer de haut
en bas avec les flèches Up et Down du clavier. On peut aussi le faire tirer en 
cliquant sur la barre espace du clavier.

Une fois qu'on a fait tirer notre personnage, il expulse un projectile qui ce dirige
vers la droite de notre écran.

	--ennemis--
A droite de l'écran de jeu, des ennemies arrivent de manière aléatoire sur la 
première ou deuxième plateforme. Une fois qu'un ennemi arrive au bout d'une 
platforme, il vole a l'aide d'un ballon qui s'affiche au-dessus de lui à ce
moment-là. 

Une fois que l'ennemi arrive en bas de l'écran, son ballon disparaît et il ce dirige
vers notre personnage. Quand l'ennemi arrive au bout de l'écran(à gauche), il 
s'arrête et ce pose là.
Si il y a plusieurs ennemies qui ce posent, Les ennemies ce posent les uns au dessus 
des autres(comme des tortues :)).

Si notre personnage touche un ennemie(quand l'ennemie est posé donc), il meurt.
Dans ce cas un écran gameover s'affiche et on peut de là recommencer le jeu du début.

Pour éviter que notre personnage meurt, il faut qu'il détruise les ennemies à l'aide de
ces projectiles avant que les ennemies arrivent en bas de l'écran. Attention si un
projectile touche le ballon d'un ennemi, l'ennemi tombe vers le bas de l'écran. 
Il est donc dans ce cas très difficile de tuer l'ennemi en question avant 
qu'il arrive en bas de l'écran. 

Quand les ennemies arrivent en bas de l'écran on ne peut plus les atteindre avec nos
projectiles.
Quand on détruit un ennemi on gagne un point(nombre de points affiché en bas de 
l'écran à droite).