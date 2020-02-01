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
[INFO] Total amount of tokens in the bag:  137
Fortress: 	2x Valk    
Fortress: 	1x Mead    1x Cows    1x Gold    
Fortress: 	2x Mead    
Fortress: 	2x Mead    
Fortress: 	1x Jarl    1x Gold    
Fortress: 	1x Jarl    1x Cows    1x Gold    
 
Monastery: 	1x Cows    1x Iron    1x Gold    
Monastery: 	2x Mead    
Outpost: 	2x Mead    1x Iron    
Outpost: 	1x Jarl    2x Mead    
Monastery: 	2x Iron    
Monastery: 	1x Mead    2x Gold    
 
Harbour: 	2x Mead    1x Gold    1x Cows    
Harbour: 	1x Mead    1x Gold    1x Cows    
Harbour: 	1x Jarl    2x Mead    1x Gold    
Outpost: 	2x Jarl    1x Gold    1x Valk    
Outpost: 	1x Cows    1x Iron    1x Valk    
 
Harbour: 	2x Mead    1x Valk    
Harbour: 	2x Jarl    1x Mead    1x Cows    
Harbour: 	2x Mead    1x Jarl    1x Cows    
 
Harbour: 	1x Mead    1x Cows    1x Gold    1x Valk    
Harbour: 	2x Cows    1x Gold    
Harbour: 	1x Mead    1x Iron    2x Gold    
 
Township: 	1x Cows    2x Iron    1x Gold    
Township: 	1x Jarl    1x Gold    1x Valk    
Township: 	1x Mead    2x Valk    1x Cows    
```