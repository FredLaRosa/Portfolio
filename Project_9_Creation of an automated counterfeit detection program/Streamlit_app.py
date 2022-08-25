#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#####################################################
# Importation des fonctions et/ou classes externes: #
# ------------------------------------------------- #
#                                                   #
import streamlit as st
import pandas as pd
from joblib import load
from PIL import Image
from prince import PCA as prince_PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.text import Text
import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerPatch
# Application du style "darkgrid" par défaut
sns.set_style("darkgrid")
#                                                   #
#####################################################

################################################################################
# Paramètres d'affichage de la data app sur le web :                           #
# ---------------------------------------------------------------------------- #
#                                                                              #
st.set_page_config(page_title="Détecter les faux billets", page_icon=":euro:")
#                                                                              #
################################################################################

########################################################################################################
# Préparation du dataset pour créer le modèle:                                                         #
# ---------------------------------------------------------------------------------------------------- #
#                                                                                                      #
billets_final = pd.read_csv(
    r"C:\Users\ElMeTeOr\Desktop\Data_Anlyst_Projets\P10_La_Rosa_Frédéric\billets_final.csv"
)

####################################################################################
# Importation des modèles de prédiction; d'ACP; de preprocessing; objets pour      #
# graphique et dataset :                                                           #
# -------------------------------------------------------------------------------- #
#                                                                                  #
logit_full_rbs, prince_pca, rbs, std_non_reduites = load(
    "logit_acp_rbs_stdns_pred_nat_bill.joblib")

billets_test_prod_centre_non_reduit, pcs, pca_row_coord, n_labels,
colors = load("data_pcs_rowcoord_nlab_col_pred_nat_bill.joblib")
#                                                                                  #
####################################################################################


########################################################################################################
# Création des classes pour notre gestionnaire de légende:                                             #
# ---------------------------------------------------------------------------------------------------- #
#                                                                                                      #
# Pour les entiers
class IntHandler:

    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        text = Text(x0, y0, str(orig_handle), color="red", fontsize=16)
        handlebox.add_artist(text)
        return text


# Pour les ellispes
class HandlerEllipse(HandlerPatch):

    def create_artists(self, legend, orig_handle, xdescent, ydescent, width,
                       height, fontsize, trans):
        center = 0.5 * width - 0.5 * xdescent, 0.5 * height - 0.5 * ydescent
        p = mpatches.Ellipse(xy=center,
                             width=width + xdescent,
                             height=height + ydescent)
        self.update_prop(p, orig_handle, legend)
        p.set_transform(trans)
        return [p]


#                                                                                                      #
########################################################################################################

########################################################################################################
# Préparation des données pour l'ACP:                                                                  #
# ---------------------------------------------------------------------------------------------------- #
#                                                                                                      #
billets_ACP_centree = billets_final.copy()
billets_ACP_centree = billets_ACP_centree.set_index("is_genuine")

std_non_reduites = StandardScaler(with_std=False)

billets_ACP_centree_non_reduite = pd.DataFrame(
    std_non_reduites.fit_transform(billets_ACP_centree),
    index=billets_ACP_centree.index,
    columns=billets_ACP_centree.columns)

# Ajustement de l'ACP
prince_pca = prince_PCA(n_components=2,
                        n_iter=3,
                        rescale_with_mean=True,
                        rescale_with_std=False,
                        copy=True,
                        check_input=True,
                        engine="auto",
                        random_state=42)
prince_pca = prince_pca.fit(billets_ACP_centree_non_reduite)
#                                                                                                      #
########################################################################################################

########################################################################################################
# Préparation des données pour l'affichage biplot:                                                     #
# ---------------------------------------------------------------------------------------------------- #
#                                                                                                      #
# On labellise le nom des variables par un chiffre
n_labels = [
    value
    for value in range(1, (len(billets_ACP_centree_non_reduite.index) + 1))
]

# Coordonnées des composantes
pcs = prince_pca.column_correlations(billets_ACP_centree_non_reduite)

# Coordonnées des individus
pca_row_coord = prince_pca.row_coordinates(
    billets_ACP_centree_non_reduite).to_numpy()

# Préparation des couleurs pour le pramètre "c"
colors = billets_ACP_centree_non_reduite.index.map({
    "True": 1,
    "False": 0
}).to_numpy()
#                                                                                                      #
########################################################################################################

########################################################################################################
# Création des conteneurs:                                                                             #
# -----------------------------------------------------------------------------------------------------#
#                                                                                                      #
image = st.container()
header = st.container()
intro = st.container()
presentation = st.container()
loading = st.container()
#                                                                                                      #
########################################################################################################

########################################################################################################
# Configuration des conteneurs:                                                                        #
# -----------------------------------------------------------------------------------------------------#
#                                                                                                      #
with image:
    image = Image.open(
        r"C:\Users\ElMeTeOr\Desktop\Data_Anlyst_Projets\P10_La_Rosa_Frédéric\Logo ONCFM.png"
    )
    st.image(image, caption="Logo ONCFM")

with header:
    st.title("Détection des faux billets")

with intro:
    st.subheader("Contexte")
    st.write(
        """Selon l'office central de la répression du faux monnayage (OCRFM), plus de 600 000 
faux billets de banque circulent en France chaque année. Avec les réseaux de la Camorra, du 
grand banditisme, des « officines » et du Darknet… il est assez facile aujourd'hui de se 
procurer de faux billets, se revendant en moyenne 70% moins cher de leur valeur d'origine. 

Sur l'ensemble des faux billets imprimés, 2/3 correspondent à des petites coupures de 20€ et 50€, 
générant des pertes financières pour les petits commerces, particuliers, ... impactés le plus
par ces escroqueries.

Pour accompagner les consommateurs, la Banque centrale européenne préconise d’appliquer une 
méthode (TRI) d’identification simple : la méthode Toucher, Regarder, Incliner. 
Le travail et le talent de certains faussaires, couplés aux progrès technologiques, ont rendu 
difficile la détection des faux billets grâce à l'œil nu et au toucher. 
Afin d'aider les personnes ayant un doute, des outils technologiques ont été créés afin de mieux les détecter :
- stylo à encre volatile, restant transparente et s’estompant sur un billet authentique,
et se colorant si elle est appliquée sur un faux billet ;
- détecteurs de faux billets à lampe UV ou infrarouge, identifiant des composants anormaux sur des billets falsifiés ;
- détecteurs automatiques, capables d’analyser tous les points d’authenticité d'un billet.
""")

with presentation:
    st.subheader("Détection automatique grâce à la Data Science")
    st.write(
        """A l'instar de l'ingéniosité grandissante de certains faussaires, la Data Science évolue 
aussi, offrant un panel d'outils qui améliore la qualité de détection des faux billets, et ce, 
s'appuyant sur divers critères comme les dimensions géométriques de ces derniers.

En analysant un jeu de données comportant les données géométriques de 1500 billets, dont 1000 Vrai
et 500 Faux, nous avons pu -grâce à l'analyse factorielle et à des algorithmes de Machine Learning-
créer un modèle prédisant à 99,20% (score de performance moyen obtenu sur l'ensemble des tests réalisés,
oscillant entre 98.67% et 100%) la nature de billets de banques.

Nous avons créé une fonction permettant de retourner, pour tout fichier *.csv* (comme le fichier
**billets_production.csv** téléchargeable sur le **GitHub** du projet
[ici](https://github.com/FredLaRosa/Streamlit_Project_1/blob/main/billets_production.csv)) contenant les
données géométriques de billets de banques
et respectant une certaine nomenclature, un tableau indiquant pour chaque billet, ses dimensions,
sa nature -*True* pour vrai, *False* pour faux- ainsi que le score de probabilité attestant de sa nature.

Nous afficherons les billets testés dans un bibplot, ce dernier affichant la projection des individus
(billets) et du cercle des corrélations obtenu lors de l'analyse factorielle du jeu de donnée ayant servi
à ajuster notre modèle de prédiction.

L'ACP nous montre bien que la nature des billets est observable sur l'axe F1 avec les variables **length**
et **margin_low** qui en sont les mieux représentées dans le cercle des corrélations. Les billets ayant 
une petite longueur (**length**), une marge inférieure et supérieure (**margin_low** et **margin_up**), 
ainsi qu'une hauteur gauche-droite (**height_left** et **height_right**) plus grande, sont considérés comme faux."""
    )

with loading:
    st.header("Utilisation du programme de prédiction")
    st.write(
        """Pour détecter la nature des billets, merci de cliquer sur l'onglet **Browse files**
et d'insérer votre jeu de donnée en format *csv*.""")
    sel_col, disp_col = st.columns(2)

    uploaded_file = sel_col.file_uploader("Uploader un fichier")
    ###################################################################################
    # Application de la prédiction sur le fichier uploadé:                            #
    # ------------------------------------------------------------------------------- #
    #                                                                                 #
    if uploaded_file is not None:
        dataset = pd.read_csv(uploaded_file)
        dataset = dataset.dropna()
        if dataset.columns.str.contains("id", case=False).any():
            dataset = dataset.set_index("id")

        dataset = dataset.loc[:, [
            "diagonal", "height_left", "height_right", "margin_low",
            "margin_up", "length"
        ]]
        # Normalisation des données avec l'objet rbs utilisé pour centrer
        # les données du modèle logit_full_rbs
        dataset_rbs = pd.DataFrame(rbs.transform(dataset),
                                   index=dataset.index,
                                   columns=dataset.columns)

        # Application du modèle de régression logistique "logit_full_rbs"
        tadam = logit_full_rbs.predict(dataset_rbs)

        # Création d'un df retournant les résultats de la prédiction
        resultat = dataset.copy()
        resultat["Nature"] = tadam
        resultat[["Proba Faux", "Proba Vrai"
                  ]] = logit_full_rbs.predict_proba(dataset_rbs).round(2)
        resultat["Nature"] = resultat["Nature"].map({1: "True", 0: "False"})
        #                                                                                 #
        ###################################################################################

        ###################################################################################
        # Affichage du biplot des individus et variables avec les billets testés:         #
        # ------------------------------------------------------------------------------- #
        #                                                                                 #
        #                                                                                 #
        # Calcul des coordonnées des billets à tester du fichier "dataset":               #
        # ---------------------------------------
        #
        # Preprocessing avec le même modèle utilisé pour obtenir le dataframe
        # "billets_ACP_centree_non_reduite"
        billets_test_prod_centre_non_reduit = pd.DataFrame(
            std_non_reduites.transform(dataset),
            index=dataset.index,
            columns=dataset.columns)
        #                                                                                 #
        #                                                                                 #
        # Paramétrage du biplot:                                                          #
        # ---------------------------------------                                         #
        #                                                                                 #
        # On affiche la projection des individus
        ax = prince_pca.plot_row_coordinates(
            billets_ACP_centree_non_reduite,
            figsize=(12, 12),
            x_component=0,
            y_component=1,
            labels=None,
            color_labels=billets_ACP_centree_non_reduite.index,
            ellipse_outline=True,
            ellipse_fill=True,
            show_points=True)

        # On affiche la projection des individus de "billets_production"
        ax.scatter(x=prince_pca.row_coordinates(
            billets_test_prod_centre_non_reduit)[0],
                   y=prince_pca.row_coordinates(
                       billets_test_prod_centre_non_reduit)[1],
                   color="#ffe66d",
                   marker="^",
                   s=265)

        # On trace la représentation des variables
        plt.quiver(np.zeros(pcs.to_numpy().shape[0]),
                   np.zeros(pcs.to_numpy().shape[0]),
                   pcs[0],
                   pcs[1],
                   angles="xy",
                   scale_units="xy",
                   scale=1,
                   color="r",
                   width=0.003)

        # On affiche le nom des variables
        for i, (x, y) in enumerate(zip(pcs[0], pcs[1])):
            plt.text(x,
                     y,
                     n_labels[i],
                     fontsize=26,
                     ha="center",
                     va="bottom",
                     color="red")

        # On affiche le nom des billets testés
        for i, (x, y) in enumerate(
                zip(
                    prince_pca.row_coordinates(
                        billets_test_prod_centre_non_reduit)[0],
                    prince_pca.row_coordinates(
                        billets_test_prod_centre_non_reduit)[1])):
            plt.text(x,
                     y,
                     billets_test_prod_centre_non_reduit.index[i],
                     fontsize=26,
                     ha="center",
                     va="bottom",
                     color="#ffe66d")

        # On trace un cercle
        circle = plt.Circle((0, 0),
                            1,
                            facecolor="none",
                            edgecolor="#fa912e",
                            linewidth=2,
                            label="Cercle des corrélations")
        # On ajoute notre cercle au graphique
        plt.gca().add_artist(circle)

        # Titre
        plt.title("Biplot des individus et des variables", fontsize=22)

        # X et Y labels retournant le % d'inertie
        plt.xlabel("F{} ({}%)".format(
            1, round(100 * prince_pca.explained_inertia_[0], 1)),
                   fontsize=16)
        plt.ylabel("F{} ({}%)".format(
            2, round(100 * prince_pca.explained_inertia_[1], 1)),
                   fontsize=16)

        # Légende des variables
        legend_1 = plt.legend(n_labels,
                              pcs.index,
                              handler_map={int: IntHandler()},
                              bbox_to_anchor=(1, 1),
                              fontsize=16)

        # Création d'une légende pour les scatter plot
        true_patch = mpatches.Patch(color="#9fc377", label="True")
        false_patch = mpatches.Patch(color="#0272a2", label="False")
        billets_prod = mpatches.Patch(color="#ffe66d", label="Billets testés")

        plt.legend(handles=[true_patch, false_patch, billets_prod, circle],
                   handler_map={
                       int: IntHandler(),
                       mpatches.Circle: HandlerEllipse()
                   },
                   bbox_to_anchor=(1, 0.75),
                   fontsize=16)

        # Affichage de la legend_1
        plt.gca().add_artist(legend_1)

        # Affichage d'une grille pour faciliter la lecture des coordonnées
        plt.grid(visible=True)
        #                                                                                 #
        ###################################################################################

        st.subheader("Résultat de la prédiction")
        # Affichage du DataFrame "resultat"
        st.dataframe(
            resultat.style.format(subset=[
                "diagonal", "height_left", "height_right", "margin_low",
                "margin_up", "length", "Proba Faux", "Proba Vrai"
            ],
                                  formatter="{:.2f}"))

        st.subheader(
            "Affichage des billets testés sur le biplot des individus et variables"
        )
        # On retire le message d'error car "fig" n'est pas appelé directement
        st.set_option("deprecation.showPyplotGlobalUse", False)
        # Affichage du Biplot
        st.pyplot()