- Real-time management
- randomly generated play field
- some amount of entities to manage
- internal values contribute towards some total that is freely given
- internal values can be deduced by some affects around entity

# Dungeon Master
- You are the master of a dungeon and must cater towards the enemies in your dungeon, and must keep them alive for as long as possible.
- Values on enemies:
	- Health (deducted by adventurers)
	- Morale
	- Strength
	- Speed
	- tbd
- Adventurers show up to the dungeon and fight after some time period

# Algorithms
*This list does not consider parameters, unless specified
- Account
	- temp
- Leaderboard
	- simple database calls
		- getTop()
			- Returns list of top players and stats about them
		- getClose()
			- Returns list of players within $\pm 10$ of you, and stats
- Game
	- generateDungeon()
		- Creates the initial playfield for the game, including base troops, their stats, room layout, etc. ___try to make it seed-based.
		- 