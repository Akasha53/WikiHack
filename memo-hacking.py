def display_banner():
    banner = r"""
    _   _           _         
   /_\ | |____ _ __| |_  __ _
  / _ \| / / _` (_-< ' \/ _` |
 /_/ \_\_\_\__,_/__/_||_\__,_|
                                                                                                              
"""
    print(banner)


# Dictionnaire contenant des descriptions des failles
wiki = {
    'XSS': 'Une XSS (Cross-Site Scripting) est une faille qui permet à un attaquant d\'injecter du code JavaScript malveillant pour voler des données ou manipuler une application web.',
    'XXE': 'Une XXE (XML External Entity) est une faille qui exploite les parsers XML pour lire des fichiers sensibles ou effectuer des requêtes malveillantes.',
    'SQLi': 'Une injection SQL (SQLi) permet à un attaquant d\'injecter des requêtes SQL dans une application pour lire, modifier ou supprimer des données.',
    'CSRF': 'Une attaque CSRF (Cross-Site Request Forgery) force un utilisateur authentifié à exécuter une action non désirée sur une application web.',
    'RCE': 'Une RCE (Remote Code Execution) permet à un attaquant d\'exécuter du code arbitraire à distance sur un serveur ou une machine cible.',
    'LFI': 'Une LFI (Local File Inclusion) permet à un attaquant de lire des fichiers sensibles sur le serveur via des chemins locaux.',
    'RFI': 'Une RFI (Remote File Inclusion) permet à un attaquant d\'injecter un fichier externe malveillant dans une application.',
    'IDOR': 'Un IDOR (Insecure Direct Object Reference) est une faille qui permet à un utilisateur non autorisé d\'accéder à des ressources ou données sensibles.',
    'DoS': 'Une attaque DoS (Denial of Service) vise à rendre un service indisponible en le surchargeant avec des requêtes.',
    'DDoS': 'Une attaque DDoS (Distributed Denial of Service) est une version distribuée de DoS, impliquant plusieurs machines attaquantes.',
    'Path Traversal': 'Cette faille permet à un attaquant de naviguer dans l\'arborescence du système de fichiers du serveur pour accéder à des fichiers sensibles.',
    'Buffer Overflow': 'Une attaque de débordement de mémoire tampon (Buffer Overflow) consiste à écraser la mémoire pour exécuter du code malveillant.',
    'Clickjacking': 'Le Clickjacking incite un utilisateur à cliquer sur des éléments invisibles ou déguisés pour exécuter des actions non désirées.',
    'MITM': 'Une attaque MITM (Man-In-The-Middle) permet à un attaquant d\'intercepter et modifier les communications entre deux parties.',
    'Brute Force': 'Une attaque par Brute Force consiste à essayer toutes les combinaisons possibles pour casser un mot de passe ou une clé de chiffrement.',
    'DNS Spoofing': 'Le DNS Spoofing redirige une requête DNS légitime vers un site contrôlé par l\'attaquant.',
    'Subdomain Takeover': 'Une prise de contrôle de sous-domaine permet à un attaquant d\'exploiter un sous-domaine mal configuré pour héberger du contenu malveillant.',
    'Privilege Escalation': 'Une escalade de privilèges permet à un attaquant d\'augmenter ses droits pour accéder à des ressources ou exécuter des commandes interdites.',
    'Code Injection': 'Une injection de code permet à un attaquant d\'exécuter du code malveillant dans une application vulnérable.',
    'Directory Listing': 'Cette faille expose l\'arborescence d\'un répertoire sur un serveur, révélant des fichiers sensibles.'
}

# Dictionnaire contenant des exemples pour chaque faille
exemple = {
    'XSS': '<script>alert("XSS")</script>',
    'XXE': '<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>',
    'SQLi': "' OR 1=1 -- -",
    'CSRF': '<img src="http://victime.com/dangerous_action" />',
    'RCE': 'os.system("rm -rf /")',
    'LFI': '/etc/passwd',
    'RFI': 'http://malicious.com/shell.php',
    'IDOR': 'http://victime.com/user/1234 -> Remplacez par 5678',
    'DoS': 'Exemple: Envoyer des requêtes massives avec un outil comme LOIC.',
    'DDoS': 'Exemple: Botnet générant 1M de requêtes simultanées.',
    'Path Traversal': '../../../../etc/passwd',
    "Buffer Overflow": 'A * 5000 (chaine trop longue envoyée en entrée)',
    'Clickjacking': '<iframe src="http://victime.com" style="opacity:0;"></iframe>',
    'MITM': 'Exemple: Interception avec un outil comme Wireshark ou ettercap.',
    'Brute Force': 'Exemple: Utilisation d’un outil comme Hydra pour tester des mots de passe.',
    'DNS Spoofing': 'Exemple: Redirection via un serveur DNS corrompu.',
    'Subdomain Takeover': 'Exemple: Exploitation d\'un enregistrement CNAME orphelin.',
    'Privilege Escalation': 'Exemple: Exploitation de failles dans un kernel Linux.',
    'Code Injection': 'Exemple: Ajouter ; ls dans un champ de commande.',
    'Directory Listing': 'Exemple: Accéder à http://victime.com/ répertorie tous les fichiers.'
}

def lister_cles_wiki():
    print("Liste des failles disponibles :")
    for cle in wiki.keys():
        print(f"- {cle}")


def memo_hacking(word: str):
    """
    Fonction qui affiche des informations sur une faille donnée.
    """
    if word in wiki:
        print(f"Description de la faille {word} :")
        print(wiki[word])
        print("\nExemple d'exploitation :")
        print(exemple[word])
    else:
        print(f"Aucune information disponible pour la faille : {word}.")


if __name__ == "__main__":
    print("Bonjour, cet outil permet de ressortir des infos sur une faille en hacking.")
    display_banner()

    while True:
        x = input("Voulez-vous lister les entrées du wiki ? (oui/non) : ").strip().lower()
        if x == "oui":
            lister_cles_wiki()
            break
        elif x == "non":
            break
        else:
            print("Mauvais argument saisi, veuillez entrer 'oui' ou 'non'.")

    while True:
        word = input("Entrez le nom d'une faille (par exemple : XSS, SQLi, LFI, MITM, etc.) ou 'quit' pour quitter : ").strip()
        if word.lower() == "quit":
            print("Au revoir !")
            break
        memo_hacking(word)