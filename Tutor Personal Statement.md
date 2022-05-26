```                                                                    mermaid
flowchart TB
    A[Main Menu] --> B
    users[(Account DB)]
    B[Login Screen] o--> users
    B --> Game[Gameplay] & Stats[Stats] & Cog[Settings]
    Game --> C[Creation Menu]
    C --> Cd([Can enter values to\nsetup the game you want])
    C --> D[Actual Gameplay]
```
