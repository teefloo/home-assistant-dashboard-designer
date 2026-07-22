# Architecture et design

Charge ce fichier pour concevoir les dashboards, vues, composants, responsive et hiérarchie visuelle.

## Séparation recommandée

### Dashboard Maison

- Accueil : contexte, alertes, actions, pièces.
- Pièces : accès détaillé ou vue agrégée.
- Énergie : suivi et analyse.
- Sécurité : alarme, ouvertures, caméras et événements.

### Dashboard Murale

- une ou deux vues maximum ;
- commandes tactiles larges ;
- informations familiales et contextuelles ;
- pas de maintenance système ;
- luminosité, veille et reconnexion testées ;
- caméra ou sonnette seulement à la demande.

### Dashboard Admin

- intégrations et mises à jour ;
- batteries ;
- indisponibilités ;
- réseau, hôte et stockage ;
- actions de redémarrage protégées ;
- visibilité administrateur.

## Dashboard Accueil

### Contexte global

Afficher seulement les états consultés quotidiennement : météo, présence, alarme, ouvertures, température extérieure, consommation instantanée.

### Alertes

Une alerte doit être actionnable. Afficher le problème, le contexte, la gravité et l'action utile. Masquer toute la section lorsqu'elle est vide.

### Actions rapides

Créer des intentions : mode nuit, départ, retour, tout éteindre, fermer les volets, lancer l'aspirateur. Limiter à quatre ou six actions.

### Pièces

Chaque carte de pièce suit le même contrat :

- nom et icône ;
- état principal ;
- une ou deux métriques secondaires ;
- indicateur d'anomalie ;
- accès au détail ;
- trois ou quatre commandes secondaires maximum.

### Contenu contextuel

Média, climat, tâches ou caméra apparaissent uniquement lorsqu'ils sont actifs ou pertinents.

## Pop-up ou sous-vue

Utiliser un pop-up pour une interaction courte : lumières, volets, climat, média, quelques capteurs. Utiliser une sous-vue pour un contenu long, plusieurs graphiques, caméras, historique ou plan d'étage.

## Design system

### Espacement

Utiliser une échelle réduite, par exemple 4, 8, 12, 16, 24 et 32 px. Ne pas choisir une marge différente pour chaque carte.

### Formes

Choisir un rayon global et une variante compacte. Éviter de mélanger cartes carrées, pilules et cercles sans fonction claire.

### Couleurs

- neutre : inactif ou normal ;
- accent : actif ;
- bleu : information ;
- vert : succès confirmé ;
- orange : attention ;
- rouge : danger ou erreur.

Ne pas coder deux significations avec la même couleur. Ajouter texte ou icône aux alertes pour l'accessibilité.

### Typographie

Limiter une carte à un titre, une valeur principale et une information secondaire. Les unités doivent être cohérentes. Éviter les libellés tronqués et le texte centré sur plusieurs lignes.

### Icônes

Utiliser une famille cohérente, généralement Material Design Icons. L'icône complète le texte mais ne doit pas être le seul porteur de sens pour une action sensible.

## Responsive

### Mobile

- une colonne logique ;
- actions accessibles au pouce ;
- pas de tableaux larges ;
- pop-ups courts ;
- informations prioritaires avant le premier scroll ;
- navigation stable.

### Tablette murale

- éléments tactiles plus grands ;
- contraste adapté à la distance ;
- densité modérée ;
- aucune action dangereuse au premier niveau ;
- tester orientation, veille et mode kiosque éventuel.

### Desktop

- exploiter la largeur sans créer des lignes trop longues ;
- conserver les mêmes composants et la même hiérarchie ;
- utiliser les colonnes supplémentaires pour le détail, pas pour tout afficher.

## Patterns d'état

Chaque composant doit prévoir :

- état normal ;
- actif ;
- alerte ;
- `unknown` ;
- `unavailable` ;
- valeur absente ;
- valeur hors seuil ;
- permission insuffisante ;
- liste vide.

## Anti-patterns

- plan d'étage comme unique navigation ;
- chaque pièce avec une couleur décorative différente ;
- cartes géantes pour des capteurs secondaires ;
- dix graphiques sur l'accueil ;
- contrôle appareil par appareil lorsque l'utilisateur pense en scènes ;
- données administratives visibles par tous ;
- actions critiques au simple tap sans confirmation ;
- responsive basé uniquement sur des cartes conditionnelles dupliquées.