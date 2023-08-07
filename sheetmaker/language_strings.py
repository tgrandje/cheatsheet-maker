"""Language selector handler

Todo:
    * Use internacionalization
    * Add more languages 
"""

french = {
    "INTRO_MESSAGE" : "Bienvenue",
    "MAIN_MENU_OPTIONS" : { 1: "Créer une cheatsheet",
                            2: "Sortir",
                            },
    "MENU_MESSAGE" : "Indiquer votre choix",
    "CONFIG_SHEET_MESSAGE1" : "Construction du template... Répondez aux questions suivantes.",
    "CONFIG_SHEET_MESSAGE2" : "Combien de colonnes doit-il y avoir ?",
    "CONFIG_SHEET_MESSAGE3" : "Quelle couleur souhaitez-vous ?",
    "CONFIG_SHEET_OPTIONS1" : { 1: "Quel est votre titre ?"
                            },
    "CONFIG_SHEET_OPTIONS2" : { 1: "1 colonne",
                                2: "2 colonnes",
                                3: "3 colonnes"
                            },
    "CONFIG_SHEET_OPTIONS3" : { 1: "Orange",
                                2: "Noir et blanc",
                                3: "Rouge",
                                4: "Jaune",
                                5: "Vert",
                                6: "Bleu",
                            },
    "HEADER_MESSAGE" : "Construction de l'entête... Répondez aux questions suivantes.",
    "HEADER_OPTIONS1" : { 1: "Quel est le nom de l'auteur ?"
                        },
    "HEADER_OPTIONS2" : { 1: "Quel est le nom de l'employeur ?"
                        },
    "HEADER_OPTIONS3" : { 1: "Quel est le site internet à référencer (https://...) ?"
                        },
    "BLOCK_MESSAGE" : "Construction des blocs... Répondez aux questions suivantes.",
    "BLOCK_OPTIONS" : { 1: "Créer un bloc de texte",
                        2: "Créer un bloc multilignes",
                        0: "Terminé"
                    },
    "BLOCK_ROWS_MESSAGE1" : "Construction d'un bloc multilignes... Répondez aux questions suivantes.",
    "BLOCK_ROWS_MESSAGE2" : "Dans quelle colonne voulez-vous insérer le bloc ?",
    "BLOCK_ROWS_OPTIONS1" : { 1: "Quel est le titre du bloc ?"
                            },
    "BLOCK_ROWS_OPTIONS2" : { 1: "Combien de lignes doit-il avoir ?"
                            },
    "BLOCK_ROWS_OPTIONS3" : { 1: "Quel est le texte des lignes ? (Format = 'text1 # text2 # text3')"
                            },
    "TEXT_BLOCK_MESSAGE" : "Construction du bloc de text... Répondez aux questions suivantes.",
    "TEXT_BLOCK_EXTRA" : "colonne",
    "TEXT_BLOCK_OPTIONS1" : { 1: "Quel est le titre du bloc ?"
                            },
    "TEXT_BLOCK_OPTIONS2" : { 1: "Quel est le texte du block ? (utilisez <br> pour une nouvelle ligne ou n'importe quel tag html pour du formattage)"
                            },
    "END_MESSAGE" : "Merci",
    "EXIT_MESSAGE" : "Appuyez sur n'importe quelle touche pour quitter",
    "INVALID_INPUT_MESSAGE" : "Entrée invalide, réessayez.",
}

