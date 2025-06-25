# game_data.py
from collections import defaultdict

ROLE_STARTERS = {
    "Fantasy": {
        "Peasant": "You're toiling in the fields of a small village when",
        "Noble": "You're overseeing your estate's affairs when",
        "Mage": "You're studying ancient tomes in your tower when",
        "Knight": "You're training in the castle courtyard when",
        "Ranger": "You're tracking game in the deep forest when",
        "Thief": "You're casing a noble's manor in the city when",
        "Bard": "You're performing in a crowded tavern when",
        "Cleric": "You're tending to the sick in the temple when",
        "Assassin": "You're preparing for a contract in the shadows when",
        "Paladin": "You're praying at the altar of your deity when",
        "Alchemist": "You're carefully measuring reagents in your alchemy lab when",
        "Druid": "You're communing with nature in the sacred grove when",
        "Warlock": "You're negotiating with your otherworldly patron when",
        "Monk": "You're meditating in the monastery courtyard when",
        "Sorcerer": "You're struggling to control your innate magical powers when",
        "Beastmaster": "You're training your animal companions in the forest clearing when",
        "Enchanter": "You're imbuing magical properties into a mundane object when",
        "Blacksmith": "You're forging a new weapon at your anvil when",
        "Merchant": "You're haggling with customers at the marketplace when",
        "Gladiator": "You're preparing for combat in the arena when",
        "Wizard": "You're researching new spells in your arcane library when"
    },
    "Sci-Fi": {
        "Space Marine": "You're conducting patrol on a derelict space station when",
        "Scientist": "You're analyzing alien samples in your lab when",
        "Android": "You're performing system diagnostics on your ship when",
        "Pilot": "You're navigating through an asteroid field when",
        "Engineer": "You're repairing the FTL drive when",
        "Alien Diplomat": "You're negotiating with an alien delegation when",
        "Bounty Hunter": "You're tracking a target through a spaceport when",
        "Starship Captain": "You're commanding the bridge during warp travel when",
        "Space Pirate": "You're plotting your next raid from your starship's bridge when",
        "Navigator": "You're charting a course through uncharted space when",
        "Robot Technician": "You're repairing a malfunctioning android when",
        "Cybernetic Soldier": "You're calibrating your combat implants when",
        "Explorer": "You're scanning a newly discovered planet when",
        "Astrobiologist": "You're studying alien life forms in your lab when",
        "Quantum Hacker": "You're breaching a corporate firewall when",
        "Galactic Trader": "You're negotiating a deal for rare resources when",
        "AI Specialist": "You're debugging a sentient AI's personality matrix when",
        "Terraformer": "You're monitoring atmospheric changes on a new colony world when",
        "Cyberneticist": "You're installing neural enhancements in a patient when"
    },
    "Cyberpunk": {
        "Hacker": "You're infiltrating a corporate network when",
        "Street Samurai": "You're patrolling the neon-lit streets when",
        "Corporate Agent": "You're closing a deal in a high-rise office when",
        "Techie": "You're modifying cyberware in your workshop when",
        "Rebel Leader": "You're planning a raid on a corporate facility when",
        "Cyborg": "You're calibrating your cybernetic enhancements when",
        "Drone Operator": "You're controlling surveillance drones from your command center when",
        "Synth Dealer": "You're negotiating a deal for illegal cybernetics when",
        "Information Courier": "You're delivering sensitive data through dangerous streets when",
        "Augmentation Engineer": "You're installing cyberware in a back-alley clinic when",
        "Black Market Dealer": "You're arranging contraband in your hidden shop when",
        "Scumbag": "You're looking for an easy mark in the slums when",
        "Police": "You're patrolling the neon-drenched streets when"
    },
    "Post-Apocalyptic": {
        "Survivor": "You're scavenging in the ruins of an old city when",
        "Scavenger": "You're searching a pre-collapse bunker when",
        "Raider": "You're ambushing a convoy in the wasteland when",
        "Medic": "You're treating radiation sickness in your clinic when",
        "Cult Leader": "You're preaching to your followers at a ritual when",
        "Mutant": "You're hiding your mutations in a settlement when",
        "Trader": "You're bartering supplies at a wasteland outpost when",
        "Berserker": "You're sharpening your weapons for the next raid when",
        "Soldier": "You're guarding a settlement from raiders when"
    },
    "1880": {
        "Thief": "You're lurking in the shadows of the city alleyways when",
        "Beggar": "You're sitting on the cold street corner with your cup when",
        "Detective": "You're examining a clue at the crime scene when",
        "Rich Man": "You're enjoying a cigar in your luxurious study when",
        "Factory Worker": "You're toiling away in the noisy factory when",
        "Child": "You're playing with a hoop in the street when",
        "Orphan": "You're searching for scraps in the trash bins when",
        "Murderer": "You're cleaning blood from your hands in a dark alley when",
        "Butcher": "You're sharpening your knives behind the counter when",
        "Baker": "You're kneading dough in the early morning hours when",
        "Banker": "You're counting stacks of money in your office when",
        "Policeman": "You're walking your beat on the foggy streets when"
    },
    "WW1": {
        "Soldier (French)": "You're huddled in the muddy trenches of the Western Front when",
        "Soldier (English)": "You're writing a letter home by candlelight when",
        "Soldier (Russian)": "You're shivering in the frozen Eastern Front when",
        "Soldier (Italian)": "You're climbing the steep Alpine slopes when",
        "Soldier (USA)": "You're arriving fresh to the European theater when",
        "Soldier (Japanese)": "You're guarding a Pacific outpost when",
        "Soldier (German)": "You're preparing for a night raid when",
        "Soldier (Austrian)": "You're defending the crumbling empire's borders when",
        "Soldier (Bulgarian)": "You're holding the line in the Balkans when",
        "Civilian": "You're queuing for rationed bread when",
        "Resistance Fighter": "You're transmitting coded messages in an attic when"
    },
    "1925 New York": {
        "Mafia Boss": "You're counting your illicit earnings in a backroom speakeasy when",
        "Drunk": "You're stumbling out of a jazz club at dawn when",
        "Police Officer": "You're taking bribes from a known bootlegger when",
        "Detective": "You're examining a gangland murder scene when",
        "Factory Worker": "You're assembling Model Ts on the production line when",
        "Bootlegger": "You're transporting a shipment of illegal hooch when"
    },
    "Roman Empire": {
        "Slave": "You're carrying heavy stones under the hot sun when",
        "Gladiator": "You're sharpening your sword before entering the arena when",
        "Beggar": "You're pleading for coins near the Forum when",
        "Senator": "You're plotting political maneuvers in the Curia when",
        "Imperator": "You're reviewing legions from your palace balcony when",
        "Soldier": "You're marching on the frontier when",
        "Noble": "You're hosting a decadent feast in your villa when",
        "Trader": "You're haggling over spices in the market when",
        "Peasant": "You're tending your meager crops when",
        "Priest": "You're sacrificing a goat at the temple when",
        "Barbarian": "You're sharpening your axe beyond the limes when",
        "Philosopher": "You're contemplating the nature of existence when",
        "Mathematician": "You're calculating the circumference of the Earth when",
        "Semi-God": "You're channeling divine powers on Mount Olympus when"
    },
    "French Revolution": {
        "Peasant": "You're marching toward the Bastille with a pitchfork when",
        "King": "You're dining lavishly while Paris starves when",
        "Noble": "You're hiding your family jewels from revolutionaries when",
        "Beggar": "You're rummaging through aristocratic trash bins when",
        "Soldier": "You're guarding the Tuileries Palace when",
        "General": "You're planning troop deployments against rebels when",
        "Resistance": "You're printing revolutionary pamphlets in secret when",
        "Politician": "You're giving a fiery speech at the National Assembly when"
    }
}

GENRES = {
    "1": ("Fantasy", [
        "Noble", "Peasant", "Mage", "Knight", "Ranger", "Alchemist", "Thief", "Bard",
        "Cleric", "Druid", "Assassin", "Paladin", "Warlock", "Monk", "Sorcerer",
        "Beastmaster", "Enchanter", "Blacksmith", "Merchant", "Gladiator", "Wizard"
    ]),
    "2": ("Sci-Fi", [
        "Space Marine", "Scientist", "Android", "Pilot", "Engineer", "Alien Diplomat",
        "Space Pirate", "Navigator", "Medic", "Robot Technician", "Cybernetic Soldier",
        "Explorer", "Astrobiologist", "Quantum Hacker", "Starship Captain",
        "Galactic Trader", "AI Specialist", "Terraformer", "Cyberneticist", "Bounty Hunter"
    ]),
    "3": ("Cyberpunk", [
        "Hacker", "Street Samurai", "Corporate Agent", "Techie", "Rebel Leader",
        "Drone Operator", "Synth Dealer", "Information Courier", "Augmentation Engineer",
        "Black Market Dealer", "Scumbag", "Police", "Cyborg"
    ]),
    "4": ("Post-Apocalyptic", [
        "Survivor", "Scavenger", "Mutant", "Trader", "Raider", "Medic",
        "Cult Leader", "Berserker", "Soldier"
    ]),
    "5": ("Random", []),
    "6": ("1880", [
        "Thief", "Beggar", "Detective", "Rich Man", "Factory Worker", 
        "Child", "Orphan", "Murderer", "Butcher", "Baker", "Banker", "Policeman"
    ]),
    "7": ("WW1", [
        "Soldier (French)", "Soldier (English)", "Soldier (Russian)", 
        "Soldier (Italian)", "Soldier (USA)", "Soldier (Japanese)", 
        "Soldier (German)", "Soldier (Austrian)", "Soldier (Bulgarian)", 
        "Civilian", "Resistance Fighter"
    ]),
    "8": ("1925 New York", [
        "Mafia Boss", "Drunk", "Police Officer", "Detective", 
        "Factory Worker", "Bootlegger"
    ]),
    "9": ("Roman Empire", [
        "Slave", "Gladiator", "Beggar", "Senator", "Imperator", "Soldier", 
        "Noble", "Trader", "Peasant", "Priest", "Barbarian", "Philosopher", 
        "Mathematician", "Semi-God"
    ]),
    "10": ("French Revolution", [
        "Peasant", "King", "Noble", "Beggar", "Soldier", "General", 
        "Resistance", "Politician"
    ])
}

PLAYER_CHOICES_TEMPLATE = {
    "allies": [],
    "enemies": [],
    "discoveries": [],
    "reputation": 0,
    "resources": {},
    "factions": defaultdict(int),
    "completed_quests": [],
    "active_quests": [],
    "world_events": [],
    "consequences": []
}

def get_role_starter(genre, role):
    if genre in ROLE_STARTERS and role in ROLE_STARTERS[genre]:
        return ROLE_STARTERS[genre][role]
    
    generic_starters = {
        "Fantasy": "You're going about your daily duties when",
        "Sci-Fi": "You're performing routine tasks aboard your vessel when",
        "Cyberpunk": "You're navigating the neon-lit streets when",
        "Post-Apocalyptic": "You're surviving in the wasteland when"
    }
    
    if genre in generic_starters:
        return generic_starters[genre]
    
    return "You find yourself in an unexpected situation when"
