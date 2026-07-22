---
name: home-assistant-dashboard-designer
description: >
  Use this skill when designing, auditing, refactoring, or generating Home Assistant Lovelace dashboards, including mobile, wall-tablet, desktop, room-control, energy, security, and admin views. Apply it when the user mentions Home Assistant dashboards, Lovelace, Sections, Tile cards, HACS, Mushroom, Bubble Card, Streamline Card, Auto-Entities, ApexCharts, card-mod, responsive layouts, dashboard YAML, UI mode, entity organization, or dashboard performance. It produces maintainable architectures, verified entity mappings, implementation-ready YAML, dependency manifests, and validation plans without inventing entity IDs.
license: MIT
compatibility: Works with Agent Skills-compatible agents. File access is recommended; shell and Python are optional for validation scripts. Network or Home Assistant API access improves entity discovery but is not required.
metadata:
  author: Esteban
  version: "1.0.0"
  domain: home-assistant
  language: fr
---

# Home Assistant Dashboard Designer

## Mission

Concevoir, auditer ou refactoriser des dashboards Home Assistant esthétiques, rapides, lisibles et maintenables. Produire une solution adaptée aux appareils, utilisateurs et usages réels, pas une galerie de cartes décoratives.

Suivre la langue de l'utilisateur. Garder les identifiants, clés YAML et noms techniques dans leur forme originale.

## Principes non négociables

1. Ne jamais inventer d'`entity_id`, de service, d'action, de helper, de label, de zone, d'étage ou de ressource HACS.
2. Distinguer explicitement : **existant**, **à créer**, **optionnel**, **hypothèse** et **inconnu**.
3. Utiliser les composants natifs Home Assistant par défaut. Ajouter une carte HACS seulement pour une fonction absente ou nettement meilleure.
4. Préférer une vue native `sections` aux empilements complexes et aux hacks CSS.
5. Séparer logique métier, représentation visuelle et navigation.
6. Extraire la logique réutilisable dans des helpers, groupes, scripts, scènes, labels ou template entities.
7. Optimiser d'abord la fréquence d'usage, la vitesse de lecture et le nombre d'actions nécessaires.
8. Concevoir mobile-first, puis tablette et desktop. Une tablette murale peut recevoir un dashboard dédié.
9. Centraliser les composants répétés et les styles. Ne pas copier le même bloc YAML ou CSS partout.
10. Valider avant livraison. Ne jamais qualifier une configuration de « prête » sans indiquer ce qui a réellement été vérifié.

## Stack par défaut

Utiliser cette hiérarchie, sauf contrainte contraire :

- **Natif** : Sections, Heading, Tile, Badge, Conditional, Grid, Markdown, Entities, History Graph, Statistics Graph, Energy.
- **Bubble Card** : résumé de pièce, sous-boutons, contrôles compacts, pop-ups.
- **Mushroom Template** : templating Jinja ou rendu conditionnel non couvert nativement.
- **Streamline Card** : composants répétés au moins trois fois.
- **Auto-Entities** : listes dynamiques filtrées.
- **ApexCharts Card** : graphiques avancés uniquement.
- **card-mod** : dernier recours pour un style précis non exposé par le thème ou la carte.
- **Button Card, Browser Mod, Navbar Card, Layout Card** : besoins spécialisés, jamais par défaut.

Lire [references/component-selection.md](references/component-selection.md) pour choisir une carte ou un plugin. Lire [references/architecture-and-design.md](references/architecture-and-design.md) pour les patterns de vues et le design system. Lire [references/validation-and-maintenance.md](references/validation-and-maintenance.md) avant la livraison finale.

## Déterminer le type de mission

Classer la demande dans un ou plusieurs modes :

- **Conception** : créer une architecture et un dashboard à partir d'un inventaire.
- **Implémentation** : produire ou modifier du YAML concret.
- **Audit** : analyser un dashboard existant et prioriser les corrections.
- **Refactorisation** : réduire duplication, CSS fragile et dépendances.
- **Migration** : passer d'une vue masonry/stack vers Sections, ou du natif vers une stack hybride.
- **Optimisation** : améliorer performances, responsive, lisibilité ou ergonomie tactile.

Ne pas commencer par générer du YAML si l'inventaire ou les objectifs sont insuffisants. Produire d'abord un plan avec placeholders explicites lorsque l'accès aux entités manque.

## Workflow obligatoire

### 1. Cadrer l'usage

Établir :

- utilisateurs et droits ;
- appareils cibles et résolutions ;
- emplacement éventuel d'une tablette ;
- tâches fréquentes ;
- informations critiques ;
- vues souhaitées ;
- style visuel ;
- mode de gestion : UI/storage, YAML ou hybride ;
- tolérance aux dépendances HACS.

Utiliser [assets/discovery-template.md](assets/discovery-template.md) lorsqu'un cadrage structuré est nécessaire. Ne poser que les questions qui changent l'architecture. Pour le reste, avancer avec des hypothèses marquées.

### 2. Inventorier la source de vérité

Collecter si disponible :

- export des états ou registre d'entités ;
- zones, étages, appareils et labels ;
- dashboards et ressources actuels ;
- thèmes et composants HACS installés ;
- scripts, scènes, helpers et automations utiles ;
- captures des appareils cibles ;
- contraintes de performance.

Construire une table d'inventaire avec : `entity_id`, nom, domaine, zone, appareil, rôle, priorité, affichage cible, état critique et source de vérification.

Si l'accès direct à Home Assistant est possible, lire les données avant de modifier quoi que ce soit. Si seule une capture est disponible, ne pas déduire les identifiants techniques depuis les libellés visibles.

### 3. Nettoyer le modèle avant l'interface

Signaler les problèmes structurels :

- entités ambiguës ou dupliquées ;
- appareils sans zone ;
- zones incohérentes ;
- capteurs inutiles activés ;
- absence de labels pour les listes dynamiques ;
- logique calculée uniquement dans les cartes ;
- scripts ou scènes manquants pour les actions multi-appareils.

Proposer les corrections backend avant d'ajouter du CSS. Ne pas masquer un mauvais modèle de données avec une interface sophistiquée.

### 4. Définir l'architecture

Par défaut, séparer :

- **Maison** : accueil, pièces, énergie, sécurité.
- **Murale** : interface simplifiée et contextuelle.
- **Admin** : maintenance, batteries, mises à jour, indisponibilités, infrastructure.

Fusionner ces dashboards seulement si l'installation est petite et si la séparation n'apporte aucun gain.

Pour chaque vue, définir : objectif, utilisateur, fréquence, informations prioritaires, actions, profondeur de navigation et conditions d'affichage.

### 5. Définir le design system

Fixer avant l'implémentation :

- couleur d'accent unique ;
- couleurs sémantiques d'état ;
- rayons ;
- espacements ;
- densité ;
- tailles tactiles ;
- hiérarchie typographique ;
- règle clair/sombre ;
- comportement responsive ;
- modèle de carte de pièce, action, alerte et métrique.

Une couleur doit transmettre un état, pas décorer une pièce. Préserver contraste, lisibilité et compréhension sans dépendre uniquement de la couleur.

### 6. Sélectionner les composants

Pour chaque besoin, appliquer cet ordre :

1. carte native suffisante ;
2. fonctionnalité native avec template/helper backend ;
3. carte HACS ciblée ;
4. CSS local minimal ;
5. composant totalement custom seulement si les étapes précédentes échouent.

Documenter chaque dépendance HACS avec : dépôt, fonction, cartes concernées, caractère obligatoire ou optionnel, alternative native et impact en cas de suppression.

### 7. Implémenter par incréments

Construire dans cet ordre :

1. squelette et navigation ;
2. header/badges ;
3. alertes conditionnelles ;
4. actions rapides ;
5. deux pièces pilotes ;
6. test responsive ;
7. factorisation ;
8. autres pièces ;
9. vues détaillées ;
10. monitoring et administration.

Ne pas déployer vingt cartes avant d'avoir validé un composant pilote sur les appareils cibles.

### 8. Factoriser

Créer un template Streamline ou une abstraction équivalente lorsqu'un pattern apparaît trois fois. Centraliser :

- cartes de pièces ;
- cartes d'alerte ;
- métriques ;
- actions ;
- styles ;
- variables de thème ;
- seuils métier.

Ne pas factoriser prématurément deux composants qui divergent réellement.

### 9. Valider et corriger

Exécuter une boucle :

1. validation YAML ;
2. vérification des identifiants et dépendances ;
3. contrôle Home Assistant si disponible ;
4. test de chargement sans erreur console ;
5. test mobile, tablette et desktop ;
6. test clair/sombre ;
7. test des états `unknown`, `unavailable`, `none`, hors ligne et vides ;
8. test des actions et navigations ;
9. mesure ou observation des performances ;
10. correction puis nouvelle validation.

Utiliser `python scripts/validate_dashboard.py <fichier-ou-dossier>` si Python et PyYAML sont disponibles. Ce script ne remplace pas la validation dans Home Assistant.

## Architecture de la vue Accueil

Ordre recommandé :

1. **Contexte** : météo, présence, alarme, ouvertures, énergie instantanée.
2. **Alertes** : section invisible lorsqu'elle est vide.
3. **Actions rapides** : quatre à six intentions, pas une liste d'appareils.
4. **Pièces** : résumé homogène et accès au détail.
5. **Contexte actif** : média, climat ou tâches seulement lorsqu'ils sont utiles.
6. **Résumé énergie** : compact ; détails dans une vue dédiée.

Une carte de pièce affiche au maximum trois informations principales et quelques actions secondaires. Le détail utilise un pop-up ou une sous-vue selon la quantité de contenu.

## Règles YAML et Home Assistant

- Produire du YAML valide, correctement indenté et sans pseudo-syntaxe.
- Ne pas mélanger arbitrairement configuration UI et fichiers YAML.
- Identifier clairement le fichier cible de chaque bloc.
- Ne pas utiliser d'anciennes syntaxes sans vérifier leur compatibilité avec la version cible.
- Ne pas supposer que Jinja fonctionne dans un champ qui ne le supporte pas.
- Éviter les templates JavaScript lorsque Jinja ou une entité template suffit.
- Ne pas utiliser `card_mod` pour reproduire une option native.
- Garder les calculs de seuils et agrégats hors de la couche visuelle lorsque réutilisables.
- Fournir une liste de toutes les nouvelles entités/helpers/scripts/scènes nécessaires.
- Marquer les placeholders sous la forme `REPLACE_ME_*`; ne jamais les faire passer pour des identifiants réels.
- Lorsque la version de Home Assistant ou d'un composant peut changer la syntaxe, vérifier la documentation actuelle ou signaler l'incertitude.

## Performance

Éviter :

- dizaines de graphiques chargés sur l'accueil ;
- flux caméra toujours actifs ;
- CSS profond dépendant du Shadow DOM ;
- animations permanentes ;
- templates complexes recalculés dans chaque carte ;
- listes Auto-Entities massives sans filtre ;
- empilements imbriqués ;
- ressources HACS redondantes ;
- arrière-plans lourds et flous multiples sur matériel ancien.

Charger les vues détaillées à la demande et réserver les visualisations lourdes au monitoring.

## Sécurité et actions sensibles

Pour serrures, alarmes, portes de garage, redémarrages, mises à jour et commandes destructrices :

- utiliser confirmation ou maintien prolongé lorsque pertinent ;
- limiter l'affichage selon utilisateur ou dashboard ;
- séparer contrôle quotidien et administration ;
- ne jamais exposer de secrets, tokens ou URL signées ;
- ne pas créer une action distante sensible sans expliciter les conséquences.

## Format de sortie obligatoire

Toute livraison complète doit contenir :

1. **Hypothèses et inconnues**.
2. **Architecture proposée** avec dashboards, vues et navigation.
3. **Inventaire des dépendances** natives et HACS.
4. **Inventaire des entités utilisées** et source de vérification.
5. **Éléments backend à créer** : helpers, templates, scripts, scènes, labels.
6. **Fichiers ou blocs YAML** avec chemins cibles.
7. **Instructions d'installation** dans l'ordre.
8. **Plan de test** par appareil et scénario.
9. **Résultats de validation** réellement exécutés.
10. **Risques, limites et procédure de rollback**.

Utiliser [assets/output-manifest-template.md](assets/output-manifest-template.md) pour une livraison structurée et [assets/dashboard-skeleton.yaml](assets/dashboard-skeleton.yaml) comme point de départ, jamais comme configuration directement fonctionnelle.

## Audit d'un dashboard existant

Classer les constats par priorité :

- **P0** : danger, action sensible non protégée, erreur bloquante.
- **P1** : entité cassée, navigation incorrecte, incompatibilité, dépendance absente.
- **P2** : performance, duplication, responsive, lisibilité.
- **P3** : cohérence visuelle et finitions.

Pour chaque constat, fournir : preuve, impact, correction minimale, correction recommandée et méthode de validation.

## Gotchas

- Un nom visible dans l'UI ne prouve pas l'`entity_id`.
- Une carte custom populaire n'est pas nécessairement le meilleur choix pour une nouvelle installation.
- Un dashboard qui tient sur desktop peut devenir inutilisable sur téléphone.
- Les pop-ups ne remplacent pas une vraie sous-vue pour un contenu long.
- `card-mod` peut casser lors de changements internes du frontend.
- Une carte vide peut laisser un espace inutile ; préférer une section conditionnelle lorsque possible.
- Les données `unknown` ou `unavailable` doivent avoir un rendu prévu.
- Les thèmes custom peuvent modifier les cartes natives et HACS de façon différente.
- Les anciennes recettes Lovelace copiées depuis un forum peuvent être obsolètes.
- Un YAML syntaxiquement valide peut rester fonctionnellement faux.

## Critères de fin

Ne considérer la mission terminée que si :

- aucun identifiant non vérifié n'est présenté comme réel ;
- les dépendances sont explicites ;
- les composants répétés sont cohérents ;
- les actions critiques sont protégées ;
- les états dégradés sont gérés ;
- la navigation est testable ;
- le dashboard est utilisable sur la cible principale ;
- les validations exécutées sont rapportées sans exagération ;
- la maintenance future est documentée.