Challenge technique pour l'intégration du parcours Data Scientist en alternance de la [Wide Code School](https://www.wildcodeschool.com/fr-FR/formations/formation-data-scientist).

# Objectifs du tech challenge:

Ton ancien collègue Bernardo t'appelle. Il est très inquiet. Son ordinateur est cassé et il n'avait aucune sauvegarde.
 
Il l'avait posé sur une table, et le vent l'a fait tombé. Il te l'a déjà dit 100 fois : le vent trop fort ne fait que du tort à son activité.
 
Bernardo gère les stocks de 4 boutiques. Il avait l'habitude de prévoir les ventes des prochaines semaines pour commander ses nouveaux stocks.

Il vient juste de retrouvé un ancien fichier, avec les volumes de ventes de l'année 2019 d'une seule boutique, mais il ne sait pas laquelle. Il se rappelle que tu es le Zorro de la data. Il t'appelle donc à la rescousse.


## 1. Analyse descriptive exploratoire (EDA)
Tu commenceras par explorer les données de vente [fichier ici](https://raw.githubusercontent.com/murpi/wilddata/master/test/history.csv), et tu mettras en avant notamment les saisonnalités, les produits et la complétude des données.

## 2. Trouver la boutique correspondante
Tu détermineras à quelle boutique correspond ce fichier de ventes. Pour cela, tu pourras t'aider de données météo. En effet, Bernardo nous a indiqué que les ventes sont corrélées à la météo.
Les boutiques se situent à Bordeaux, Lille, Lyon et Marseille. Tu trouveras les historiques de météo ici pour [Bordeaux](https://raw.githubusercontent.com/murpi/wilddata/master/test/bordeaux2019.csv), [Lille](https://raw.githubusercontent.com/murpi/wilddata/master/test/lille2019.csv), [Lyon](https://raw.githubusercontent.com/murpi/wilddata/master/test/lyon2019.csv), et [Marseille](https://raw.githubusercontent.com/murpi/wilddata/master/test/marseille2019.csv).

## 3. Explication de l'impact de la météo
Tu détermineras (par corrélation, ou par Machine Learning) l'importance de chaque dimension. Tu mettras en avant les variables (température, vitesse du vent, etc...) qui semblent les plus corrélées aux ventes, et celles qui sont le moins corrélées. Bernardo a-t-il raison : est-ce bien le vent qui a le plus d'impact sur les ventes ?

## 4. Prévisions de ventes
Bernardo a récupéré des prévisions météo sur une semaine [le fichier est ici](https://raw.githubusercontent.com/murpi/wilddata/master/test/forecast.csv). Il aimerait que tu lui fasses une prévision des ventes correspondant à cette période, pour qu'il puisse acheter les bons stocks de produit. Tu devras donc indiquer le stock total minimum que tu conseilles à Bernardo de commander pour la semaine prochaine, afin de pouvoir répondre à la demande, sans faire des sur-stocks.

<br>

> **Note:** Evidemment, il s'agit d'un exercice, nous ne savons donc pas exactement à quelle date tu effectueras cette analyse. Les prévisions météo sont ici pour la dernière semaine de juin. Tu dois donc effectuer des prévisions de ventes pour la dernière semaine de juin (quelle que soit la date réelle actuelle).
De même, tu partiras du principe que ces prévisions météo correspondent à la ville que tu as trouvé dans la partie 2, et que tu dois donc effectuer les prévisions de vente pour cette ville précisément.

# Quelques conseils
## Conseils pour la présentation
Bernardo n'a pas un profil technique dans la data, n'oublie donc pas dans ton analyse :
- d'expliquer toutes les notions techniques que tu utilises;
- de ne pas chercher à être exhaustif, ton rôle est de mettre en lumière les informations pertinentes, pas de crouler sous les données brutes;
- de prendre du recul sur les données, avec les marges d'erreur qui s'imposent (une prévision de vente de 17,497235678 ventes pour mercredi prochain ? C'est sacrément précis...), et d'expliquer la confiance que tu as dans ton modèle de prévision;
- de présenter correctement avec des slides élégants, en respectant le temps imparti.

## Conseils pour le notebook
Le notebook doit être découpé en grandes parties.
Le code python doit être commenté, avec des variables bien nommées, etc... et si possible respecter les principes du PEP8.
Le code doit éviter au maximum les répétitions (DRY) et les copier-coller.
Le code doit idéalement être généralisable : si j'ajoute un nouveau fichier de météo pour une nouvelle ville, est-ce rapide et facile d'intégrer cette nouvelle ville à l'analyse ?
Les codes inutiles (tests, analyses préliminaires, etc...) doivent avoir été nettoyées ou supprimées.

## Conseils pour le machine learning
Tu devras être capable d'expliquer :
- ton choix d'algorithme,
- ton choix d'hyperparamètre;
- la confiance dans tes prévisions;
- les variables météo qui impactent le plus tes prévisions.
