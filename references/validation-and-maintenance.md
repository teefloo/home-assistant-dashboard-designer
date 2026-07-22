# Validation et maintenance

Charge ce fichier avant toute livraison complète, migration ou refactorisation importante.

## Validation statique

- YAML parsable ;
- chemins de fichiers corrects ;
- aucun placeholder non signalé ;
- aucune clé inventée ;
- types de cartes custom recensés ;
- ressources HACS installées ;
- entités citées présentes dans l'inventaire ;
- services/actions compatibles avec les domaines ;
- templates Jinja valides dans leur contexte ;
- navigation et ancres uniques ;
- pas de duplication accidentelle de vues ou chemins.

## Validation Home Assistant

Lorsque l'accès est disponible :

1. sauvegarder ;
2. vérifier la configuration si les fichiers backend changent ;
3. recharger les ressources ou redémarrer seulement si nécessaire ;
4. ouvrir chaque vue ;
5. inspecter les erreurs frontend ;
6. déclencher les actions non dangereuses ;
7. vérifier les entités dans Outils de développement ;
8. confirmer les permissions avec un utilisateur non administrateur.

Ne pas déclencher une serrure, une alarme ou une action destructive sans autorisation explicite.

## Tests fonctionnels

- toutes les navigations ;
- retour arrière ;
- état vide ;
- état indisponible ;
- seuils d'alerte ;
- actions rapides ;
- confirmation des actions sensibles ;
- listes dynamiques ;
- graphiques et unités ;
- thème clair et sombre ;
- cache navigateur après mise à jour HACS.

## Tests appareils

Pour chaque appareil cible, noter :

| Appareil | Résolution/orientation | Chargement | Scroll | Tactile | Lisibilité | Erreurs |
|---|---|---|---|---|---|---|

Tester au minimum le téléphone principal et l'écran mural lorsqu'il existe.

## Performance

Observer :

- délai d'affichage initial ;
- saccades au scroll ;
- utilisation CPU/mémoire de la tablette ;
- nombre de ressources custom ;
- cartes caméra ou graphiques chargés ;
- reconnexion après veille ;
- erreurs répétées console/réseau.

Corrections prioritaires : masquer ou déplacer les cartes lourdes, réduire les graphiques, désactiver les flux continus, simplifier CSS et templates, séparer les dashboards.

## Maintenance

Documenter :

- version Home Assistant testée ;
- versions HACS critiques ;
- fichiers modifiés ;
- procédure de sauvegarde ;
- procédure de rollback ;
- dépendances à surveiller ;
- zones CSS fragiles ;
- tests à refaire après mise à jour.

Après une mise à jour majeure : lire les breaking changes, tester une sauvegarde ou environnement de staging, mettre à jour les composants custom, vider le cache si nécessaire, puis exécuter les scénarios critiques.

## Rapport honnête

Employer ces formulations :

- « YAML parsé avec succès » si un parseur l'a réellement validé.
- « Références d'entités comparées à l'inventaire fourni » si cette comparaison a été faite.
- « Non testé dans Home Assistant » si aucun chargement réel n'a eu lieu.
- « Syntaxe à confirmer pour Home Assistant X.Y » si la version n'a pas été vérifiée.

Ne jamais écrire « entièrement testé » après une simple inspection visuelle du YAML.