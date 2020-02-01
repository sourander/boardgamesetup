# boardgamesetup
A helper script for board games' setup phases.

## Why?
This script was created for Raiders of the North Sea game. The game asks the player to randomize components using a bag. The 'Mead' components, however, are fairly large which makes picking them by random really difficult. Thus, one Saturday morning, I wrote a quick script.

The code should be fairly easy to modify to suit others games aswell.

## Usage
The only requirements is that you have numpy installed. After that, using the script is as simple as:
```
python raiders.py
```

An example output is:

```
Are you playing with Hall of Heroes: [y/n]: y
Are you playing with Fields of Fame: [y/n]: y
[INFO] Playing with Hall of Heroes:  True
[INFO] Playing with Fields of Fame:  True
[INFO] Total amount of cubes in the bag:  137
 
Fortress: 	1x Gold    1x Valk    
Fortress: 	2x Mead    1x Gold    
Fortress: 	1x Mead    1x Cows    
Fortress: 	1x Mead    1x Gold    
Fortress: 	1x Mead    1x Valk    
Fortress: 	1x Mead    1x Cows    1x Gold    
 
Monastery: 	1x Jarl    2x Iron    
Monastery: 	1x Mead    1x Gold    
Outpost: 	1x Mead    2x Gold    
Outpost: 	1x Cows    1x Jarl    1x Valk    
Monastery: 	1x Mead    1x Cows    
Monastery: 	1x Mead    1x Iron    1x Valk    
 
Harbour: 	1x Gold    1x Jarl    1x Iron    1x Valk    
Harbour: 	1x Mead    1x Jarl    1x Iron    
Harbour: 	1x Mead    3x Gold    
Outpost: 	2x Mead    1x Iron    1x Valk    
Outpost: 	1x Mead    1x Cows    1x Iron    
Harbour: 	2x Mead    1x Iron    
 
Harbour: 	2x Cows    1x Gold    1x Valk    
Harbour: 	2x Mead    1x Cows    1x Iron    
Harbour: 	2x Mead    1x Cows    1x Iron    
Harbour: 	3x Mead    
Harbour: 	2x Mead    1x Cows    1x Valk    
```