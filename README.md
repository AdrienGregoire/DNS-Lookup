# DNS Lookup - Python

## Description

Voici mon repo contenant un projet simple de **DNS Lookup en Python**.
Ce projet a pour but d'effectuer des recherches DNS basiques (récupération d'IP, résolution inverse, alias, etc.) pour un domaine donné.
L'objectif était de créer un outil léger, facile à lire, qui permet d’explorer le module <mark>socket</mark> de Python et de manipuler des données réseau.

## 📚 Contenu

Ce repo contient :
- <mark>SRC/lookup.py</mark> : Les fonctions permettant de récupérer les informations DNS (IP, host, alias).
- <mark>SRC/scan.py</mark> : La fonction principale <mark>dns_lookup</mark> qui orchestre l'appel des fonctions de <mark>lookup.py</mark>.
- <mark>main.py</mark> : Le point d'entrée du programme.

## Compétences développées

- Utilisation du module <mark>socket</mark> de Python
- Résolution DNS (IP, hostnames, alias)
- Organisation du code avec des modules
- Création d’un petit projet avec une structure claire et évolutive
- Retour d'erreurs simple avec <mark>try/except</mark>

## 📁 Structure du projet
```
|── SRC/
|   ├── lookup.py  # Fonctions de résolution DNS
|   └── scan.py    # Fonction principale dns_lookup
|── main.py        # Point d'entrée du programme
|── README.md      # Ce fichier
```

## Lancer le projet

Il suffit d'exécuter le script principal avec Python :
```bash
python3 main.py google.com
```
Le nom de domaine peut changer.

## Exemple de sortie
```bash
========== DNS LOOKUP ==========
Domain/IP   : google.com
IP Address  : 142.250.190.14
All Ips     : ['142.250.190.14', '142.250.190.78', ...]
Hostname    : 'par10s46-in-f14.1e100.net'
Aliases     : '[]'
=================================
```

## Licence

Aucune.
