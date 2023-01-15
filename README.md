# Jeu d'infection avec les algorithmes (minimax negamax et alphabeta)

Sécurité et aide à la décision: le projet de jeu d’infection

## Mode d'utilisation
Executer la commande suivante:

Windows:
```bash
python <taille> <profondeur_rouge> <profondeur_bleu> <algorithm>
```

Linux/MacOS:
```bash
python3 <taille> <profondeur_rouge> <profondeur_bleu> <algorithm>
```

- `<taille>`: nombre de lignes et colonnes. ex: 7 = 7x7
- `<profondeur_rouge>`: profondeur pour le joueur rouge. ex: 4
- `<profondeur_bleu>`: profondeur pour le joueur bleu. ex: 4
- `<algorithm>`: Algo a utilisé (0,1,2): 0=>minimax, 1=>negamax, 2=>alphabeta

exemple: python3 5 4 3 2

## Optionnelle
Si vous voulez generer les courbes, vous devez installer `matplotlib`

Windows:
```bash
python -m pip install -U pip
python -m pip install -U matplotlib
```

Linux/MacOS:
```bash
python3 -m pip install -U pip
python3 -m pip install -U matplotlib
```

## Membre du groupe:
- Abdoulaye Djibril DIALLO  22112788
- Mamady DJIGUINE           22110369
- Elhadj Alseiny DIALLO     22011830
- Mamadou Alpha DIALLO      22107614