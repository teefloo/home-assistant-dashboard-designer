# Sélection des composants

Charge ce fichier lorsqu'il faut choisir des cartes, réduire des dépendances HACS ou refactoriser un dashboard.

## Arbre de décision

1. Une entité simple avec une action principale : **Tile native**.
2. Un titre, un regroupement ou une navigation de section : **Heading native**.
3. Une information globale compacte : **Badge natif**.
4. Un contenu affiché selon un état : visibilité de section ou **Conditional native**.
5. Plusieurs contrôles et états dans une carte de pièce : **Bubble Card**.
6. Rendu Jinja ou logique d'affichage avancée : **Mushroom Template**.
7. Pattern répété au moins trois fois : **Streamline Card**.
8. Liste calculée depuis domaines, labels, zones ou états : **Auto-Entities**.
9. Graphique multi-séries, agrégé ou multi-axe : **ApexCharts Card**.
10. Style impossible via options ou thème : **card-mod**, local et minimal.

## Natif

### Sections

Choix par défaut pour les nouvelles vues. Utiliser la grille et les options responsive avant d'ajouter Layout Card. Préférer les sections conditionnelles aux cartes vides.

### Tile

Choix par défaut pour lumière, switch, cover, climate et entités simples. Utiliser ses features et actions natives. Ne pas la remplacer par une carte custom uniquement pour modifier un rayon ou une couleur.

### Badge

Réserver aux états globaux fréquemment consultés. Éviter une rangée de dix badges illisibles.

### Graphiques natifs

Utiliser pour un historique simple ou une statistique standard. Passer à ApexCharts seulement lorsqu'un besoin explicite l'exige.

## Bubble Card

Utiliser pour :

- résumé de pièce ;
- sous-boutons ;
- pop-ups courts ;
- contrôles compacts de climat, média ou volets ;
- cohérence tactile mobile.

Éviter pour :

- chaque capteur isolé ;
- longues pages dans un pop-up ;
- besoins couverts proprement par Tile ;
- multiplication d'effets visuels.

## Mushroom

Conserver surtout Mushroom Template et éventuellement Chips pour les cas où le natif est insuffisant. Ne pas créer un dashboard entièrement Mushroom par réflexe. Vérifier les changements de style entre versions.

## Streamline Card

Créer un template lorsqu'un composant est répété trois fois ou plus. Variables typiques : entité, nom, icône, capteur secondaire, navigation, seuils et couleur sémantique.

Ne pas cacher une logique métier complexe dans le template de carte. Le template doit composer des entités déjà propres.

## Auto-Entities

Utiliser pour :

- batteries faibles ;
- entités indisponibles ;
- ouvertures actives ;
- lumières allumées ;
- mises à jour ;
- appareils portant un label.

Préférer labels et groupes stables aux filtres basés sur des fragments de noms. Prévoir le cas liste vide.

## ApexCharts

Justifié pour :

- plusieurs séries ;
- agrégation temporelle ;
- axes multiples ;
- seuils et annotations ;
- statistiques avancées ;
- énergie, réseau ou environnement détaillé.

Éviter sur l'accueil lorsque le graphique n'aide pas une décision immédiate.

## card-mod

Autorisé pour une correction précise et centralisée. Documenter le sélecteur et le composant ciblé. Éviter les chaînes de sélecteurs internes fragiles, les animations permanentes et les copies multiples.

## Button Card

Utiliser seulement pour un composant réellement sur mesure nécessitant une grille, plusieurs champs ou logique JavaScript. Exiger une justification et un test responsive.

## Browser Mod

Utiliser pour comportements spécifiques à un navigateur ou une tablette : pop-up ciblé, écran contextuel, caméra à la sonnette. Tester consommation mémoire et comportement après reconnexion.

## Navbar Card

Envisager uniquement si la navigation native ne suffit pas et si une barre mobile persistante apporte un gain concret. Prévoir une solution de repli en cas d'incompatibilité.

## Layout Card

N'utiliser que lorsqu'une mise en page est impossible avec Sections. Une ancienne configuration fondée sur Layout Card peut être conservée si sa migration n'apporte aucun bénéfice mesurable.

## Matrice de dépendance

Pour chaque composant custom, remplir :

| Composant | Besoin | Obligatoire | Alternative native | Pages | Risque de rupture | Test de retrait |
|---|---|---|---:|---|---|---|---|
| Exemple | Pop-up pièce | Oui | Sous-vue | Accueil | Moyen | Navigation toujours accessible |