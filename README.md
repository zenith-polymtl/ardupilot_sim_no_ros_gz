# ardupilot_sim_no_ros_gz
Installation de ardupilot et de simulation de bas sans ros ni gazebo, simulation légère pour tester la création de mission


# Simulation avec Ardupilot, Gazebo et ROS2

Ce guide explique étape par étape comment installer les programmes requis pour notre projet : **WSL**, **ROS 2 Humble**, **Gazebo**, **Mission Planner** et **Ardupilot**. Des placeholders sont laissés pour insérer des images et des liens vers les sites officiels.


## 🖥️ Installation de WSL (Windows Subsystem for Linux)

### 👉 Étape 1 : Activer WSL
1. **Ouvrir un terminal** (PowerShell) et exécuter la commande suivante :
   ```bash
   wsl --install -d ubuntu-22.04
   wsl --update
   ```

## 🖥️ Installation de ROS2, Gazebo, Ardupilot et SITL pour Ardupilot 

### 👉 Étape 2 : Installation du script dans Ubuntu

   ```bash
   git clone https://github.com/ArduPilot/ardupilot.git
  cd ardupilot
  git submodule update --init --recursive
   ```



### 👉 Étape 3 : Construire la simulation

   ```bash
   ./waf configure --board sitl
  ./waf build
   ```

### 👉 Étape 3 : Lancer la simulation

   ```bash
   cd ~/ardupilot
  ./Tools/autotest/sim_vehicle.py -v ArduCopter -f quad --console --map

   ```

launch avec coordonnées de medicine hat:
   ```bash
./Tools/autotest/sim_vehicle.py -v ArduCopter -f quad --console --map -l 50.097361,110.735778,0,0
   ```


### 👉 Exemple de commandes utiles



### 👉 Exemple de contrôle du drone via Mavproxy
Cette exemple va vous permette de voir votre quadcopter décoller, faire des cercles et revenir à son point de départ.
Vous devez être connecter à Mavlink pour executer le commande (voir Étape 4)

Change to GUIDED mode, arm the throttle, and then takeoff:

   ```bash
   mode guided
   arm throttle
   takeoff 40
   ```

Change to CIRCLE mode and set the radius to 2000cm

   ```bash
   rc 3 1500
   mode circle
   param set circle_radius 2000
   ```

When you’re ready to land you can set the mode to RTL (or LAND):

   ```bash
   mode rtl
   ```



### 👉 En cas de problèmes:

Voici de commande utile dans PowerShell

En cas d'avoir besoin de réinstaller WSL2 et Ubuntu, utiliser cette commande pour déinstaller Ubuntu 22.04, puis réinstaller grâce au commande de l'étape 1:

   ```bash
   wsl --unregister Ubuntu-22.04
   ```

## 🔗 Liens Utiles

- 🌐 **Docs Ardupilot Development** : [ArduPilot Development Site](https://ardupilot.org/dev/index.html)
- 🌐 **Commandes Mavproxy** : [Mavproxy cheatsheet](https://ardupilot.org/mavproxy/docs/getting_started/cheatsheet.html)
- 🌐 **Liste de tous les paramètres d'ardupilot** : [Complete Parameter List](https://ardupilot.org/dev/docs/ros2-sitl.html)
- 🌐 **Mission Planner** : [Installing Mission Planner](https://ardupilot.org/planner/docs/mission-planner-installation.html)
- 🌐 **Commandes Mavlink** : https://ardupilot.org/dev/docs/mavlink-commands.html
- 🌐 **Docs Pymavlink** : https://mavlink.io/en/mavgen_python/
---

✨ **Bon courage pour l'installation !** 🚀

