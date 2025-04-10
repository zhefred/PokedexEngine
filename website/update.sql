BEGIN TRANSACTION;
UPDATE pokedex SET pokedex_entry = '{
"Red":          "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.", 
"Blue":         "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.", 
"Yellow":       "The bulb on its back grows by drawing energy. It gives off an aroma when it is ready to bloom.",
"Stadium":      "The bulb on its back apparently draws energy from its body. The bud is said to open into a large flower when fully grown.",

"Gold":         "Exposure to sunlight adds to its strength. Sunlight also makes the bud on its back grow larger.", 
"Silver":       "If the bud on its back starts to smell sweet, it is evidence that the large flower will soon bloom.", 
"Crystal":      "The bulb on its back grows as it absorbs nutrients. The bulb gives off a pleasent aroma when it blooms.", 
"Stadium2":     "Exposure to sunlight adds to it strength. Sunlight also makes the bud on its back grow larger. If the bud on its back starts to smell sweet, it is evidence that the large flower will soon bloom.", 

"Ruby":         "There is a bud on this Pokémon''s back. To support its weight, Ivysaur''s legs and trunk grow thick and strong. If it starts spending more time lying in the sunlight, it''s a sign that the bud will bloom into a large flower soon.", 
"Saphire":      "There is a bud on this Pokémon''s back. To support its weight, Ivysaur''s legs and trunk grow thick and strong. If it starts spending more time lying in the sunlight, it''s a sign that the bud will bloom into a large flower soon.", 
"Emerald":      "To support its bulb, Ivysaur''s legs grows sturdy. If it spends more time lying in the sunlight, the bud will soon bloom into a large flower.", 
"FireRed":      "There is a plant bulb on its back. When it absorbs nutrients, the bulb is said to blossom into a larger flower.", 
"LeafGreen":    "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.", 

"Diamond":      "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom", 
"Pearl":        "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom",
"Platinum":     "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom",
"HeartGold":    "Exposure to sunlight adds to its strength. Sunlight also makes the bud on its back grow larger.", 
"SoulSilver":   "If the bud on its back starts to smell sweet, it is evidence that the large flower will soon bloom.", 

"Black":        "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom.", 
"White":        "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom.", 
"Black2":       "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom.", 
"White2":       "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom.",

"X":            "There is a plant bulb on its back. When it absorbs nutrients, the bulb is said to blossom into a large flower", 
"Y":            "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom.", 
"Omega Ruby":   "There is a bud on this Pokémon''s back. To support its weight, Ivysaur''s legs and trunk grow thick and strong. If it starts spending more time lying in the sunlight, it''s a sign that the bud will bloom into a large flower soon.", 
"Alpha Saphire":"There is a bud on this Pokémon''s back. To support its weight, Ivysaur''s legs and trunk grow thick and strong. If it starts spending more time lying in the sunlight, it''s a sign that the bud will bloom into a large flower soon.", 

"Let''s Go Pikachu":"The bud on its back grows by drawing energy. It gives off an aroma when it is ready to bloom.", 
"Let''s Go Eevee":  "The bud on its back grows by drawing energy. It gives off an aroma when it is ready to bloom.", 

"Sword":            "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.", 
"Shield":           "Exposure to sunlight adds to its strength. Sunlight also makes the bud on its back grow larger.", 
"Brilliant Diamond":"When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom.", 
"Shining Pearl":    "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower''s coming bloom.", 

"Scarlet":      "The more sunlight Ivysaur bathes in, the more strength wells up within it, allowing the bud on its back to grow larger.",
"Violet":       "The bulb on its back grows as it absorbs nutrients. The bulb gives off a pleasant aroma when it blooms."
}' WHERE pokedex_nbr = 2;
COMMIT;