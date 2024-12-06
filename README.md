# MemoHacking Tool

## Description
**MemoHacking Tool** est un outil interactif en Python permettant d'accéder à des descriptions et exemples d'exploitation des principales failles de sécurité en hacking. Cet outil est conçu pour fournir des informations éducatives et pratiques sur les vulnérabilités courantes.

---

## Fonctionnalités

- **Affichage d'une bannière stylisée** au lancement.
- **Liste des failles disponibles** dans le dictionnaire des vulnérabilités (`wiki`).
- **Descriptions détaillées** de chaque faille, accompagnées d'exemples d'exploitation.
- **Interface utilisateur interactive** : propose des options pour explorer les informations ou quitter le programme.

---

## Utilisation

1. **Lancer le script** :
   ```bash
   python memo_hacking.py
   ```
2. L'outil affiche une bannière et vous invite à interagir :
   - **Lister les vulnérabilités** disponibles en répondant `oui` ou `non`.
   - **Rechercher une faille spécifique** en saisissant son nom (par exemple : `XSS`, `SQLi`, `LFI`, etc.).

3. Pour quitter l'outil, tapez `quit`.

---

## Exemple de sortie

**Lancement :**
```
Bonjour, cet outil permet de ressortir des infos sur une faille en hacking.

    _   _           _         
   /_\ | |____ _ __| |_  __ _
  / _ \| / / _` (_-< ' \/ _` |
 /_/ \_\_\_\__,_/__/_||_\__,_|
                                                                                                              

Voulez-vous lister les entrées du wiki ? (oui/non) :
```

**Recherche d'une faille :**
```
Entrez le nom d'une faille (par exemple : XSS, SQLi, LFI, MITM, etc.) ou 'quit' pour quitter : XSS

Description de la faille XSS :
Une XSS (Cross-Site Scripting) est une faille qui permet à un attaquant d'injecter du code JavaScript malveillant pour voler des données ou manipuler une application web.

Exemple d'exploitation :
<script>alert("XSS")</script>
```

**Quitter l'outil :**
```
Entrez le nom d'une faille (par exemple : XSS, SQLi, LFI, MITM, etc.) ou 'quit' pour quitter : quit
Au revoir !
```

---

## Contenu des dictionnaires

### Dictionnaire `wiki`
Le dictionnaire `wiki` contient les descriptions des failles les plus courantes, telles que :
- **XSS** : Cross-Site Scripting
- **SQLi** : Injection SQL
- **XXE** : XML External Entity
- **CSRF** : Cross-Site Request Forgery
- ... *(et bien d'autres)*

### Dictionnaire `exemple`
Chaque faille est accompagnée d'un exemple pratique, comme :
- **XSS** : `<script>alert("XSS")</script>`
- **SQLi** : `' OR 1=1 -- -`
- **LFI** : `/etc/passwd`

---

## Structure du code

### Fonctions principales

- **`display_banner()`** : Affiche une bannière ASCII au démarrage.
- **`lister_cles_wiki()`** : Liste toutes les failles disponibles dans le dictionnaire `wiki`.
- **`memo_hacking(word: str)`** : Affiche la description et un exemple d'exploitation pour une faille donnée.
- **Bloc principal (`if __name__ == "__main__":`)** : Gère l'interaction utilisateur.

---

## Prérequis

- **Python 3.x** : Ce programme est compatible avec les versions modernes de Python.
- **Aucune dépendance externe** n'est nécessaire.

---

## Objectif pédagogique

Cet outil vise à :
- Sensibiliser aux failles de sécurité courantes.
- Illustrer des exemples simples d'exploitation.
- Encourager la compréhension des vulnérabilités pour mieux s'en protéger.

---

## Avertissement

**Ce programme est à but éducatif uniquement.**  
L'exploitation des vulnérabilités décrites doit se limiter à des environnements contrôlés et à des fins légales. Toute utilisation malveillante est interdite et contraire à l'éthique.
