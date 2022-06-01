```
flowchart TB

    A[Main Menu] --> B

    users[(Database)] --> usersd([Stores users, secured passwords,\nand stats on games.])

    B[Login Screen] <--> users

    B --> Game[Gameplay] & Stats[Stats] & Cog[Settings]

    Stats <--> users

    Cog --> Cogd([View acc details, change details, etc.])

    Game --> C[Creation Menu]

    C --> Cd([Can enter values to\nsetup the game you want])

    C --> D[Actual Gameplay]
```