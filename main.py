
#### main.py

```python
#!/usr/bin/env python3
import random

heroes = [
    "Thalorin the Unyielding – Slain defending the last city of men, his sword still burns in the ruins.",
    "Elyra Moonblade – A sorceress lost to the void, her whispers still echo in the wind.",
    "Kadris the Titan-Slayer – Fell in battle against the last great colossus, his spear remains embedded in its skull.",
    "Darian the Betrayed – Poisoned by his own king, yet his spirit still haunts the throne.",
    "Veyl the Silent – A rogue who uncovered the gods’ secrets and was erased from history."
]

def get_random_hero():
    return random.choice(heroes)

def main():
    print("Welcome to Legends of the Fallen!")
    print("Here is a randomly generated fallen hero and their tale:")
    print(get_random_hero())

if __name__ == "__main__":
    main()
