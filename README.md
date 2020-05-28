# Exemple de tests fonctionnels sous Travis-CI

Ce dépôt contient un projet django minimal contenant un test fonctionnel pour Chrome et un pour Firefox. 
Le fichier .travis.yml configure l'intégration continue sous Travis-CI pour utiliser chromedriver et geckodriver. 
Le package **tchappui-webdriver**, ajouté au requirements.txt, a été créer afin de détecter et d'installer la version 
correcte de ces webdriver.

Pour essayer de faire tourner les tests fonctionnels en local, il suffit d'installer [chromedriver](https://chromedriver.chromium.org/downloads) 
et [geckodriver](https://github.com/mozilla/geckodriver/releases) dans le PATH et, bien entendu, d'installer Chrome et 
Firefox sur sur votre ordinateur.
