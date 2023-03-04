import random

# Lists of words to use in the lyrics

with open('adj.txt') as f:
    adj = [line.rstrip() for line in f]
with open('n.txt') as f:
    n = [line.rstrip() for line in f]
with open('v.txt') as f:
    v = [line.rstrip() for line in f]
with open('adv.txt') as f:
    adv = [line.rstrip() for line in f]

rc = random.choice
    
# Generate the lyrics
def generate_lyrics(num_nouns, num_adjectives, num_verbs, num_adverbs):
    # Use random.sample() to select num_nouns unique nouns, num_adjectives unique adjectives, num_verbs unique verbs, and num_adverbs unique adverbs
    nouns = random.sample(n, num_nouns)
    adjectives = random.sample(adj, num_adjectives)
    verbs = random.sample(v, num_verbs)
    adverbs = random.sample(adv, num_adverbs)

    # Create the first and second verse using all the selected nouns and verbs
    v1 = f"{nouns[0].capitalize()} {rc(verbs)} {nouns[1].capitalize()}, "
    v2 = f"{nouns[1].capitalize()} {rc(verbs)} {nouns[2].capitalize()}, "

    # Create the first chorus using all the selected nouns, adjectives, verbs, and adverbs
    c1 = f"{nouns[2].capitalize()} {adjectives[1].capitalize()} {nouns[0].capitalize()}, "
    c1 += f"{rc(verbs)} me to the {rc(nouns)}, "
    c1 += f"Where the {rc(nouns)} {rc(verbs)} {adverbs[0]}, and the {rc(adjectives)} {rc(nouns)} {rc(verbs)} {adverbs[1]}\n"
    c1 += f"we'll {rc(verbs)} {adverbs[2]} through the {rc(nouns)}, and {rc(verbs)} {adverbs[3]} up to the {rc(nouns)}\n"
    c1 = c1.capitalize()

    # Create the second chorus using a different set of nouns, adjectives, verbs, and adverbs
    nouns2 = random.sample(n, num_nouns)
    adjectives2 = random.sample(adj, num_adjectives)
    verbs2 = random.sample(v, num_verbs)
    adverbs2 = random.sample(adv, num_adverbs)
    c2 = f"{nouns2[2].capitalize()} {adjectives2[0].capitalize()} {nouns2[0].capitalize()}, "
    c2 += f"{rc(verbs2)} me to the {rc(nouns2)}, "
    c2 += f"Where the {rc(nouns2)} {rc(verbs2)} {adverbs2[0]}, and the {rc(adjectives2)} {rc(nouns2)} {rc(verbs2)} {adverbs2[1]}\n"
    c2 += f"I'll {rc(verbs2)} {adverbs2[2]} through the {rc(nouns2)}, and {rc(verbs2)} {adverbs2[3]} up to the {rc(nouns2)}\n"
    c2 = c2.capitalize()

    # Create the outro using all the selected nouns, verbs, and adjectives
    o = f"{nouns[0].capitalize()} {rc(verbs)} {nouns[1].capitalize()}, "
    o += f"{nouns[1].capitalize()} {adjectives[1].capitalize()} {nouns[0].capitalize()}, "
    o += f"{', '.join(nouns)}, {', '.join(verbs)}, and {', '.join(adverbs)} until the end of time."
    o = o.capitalize()
    lyrics = v1 + '\n' + c1 + '\n' + v2 + '\n' + c2 + '\n' + o
    return lyrics

num_nouns = 3
num_adjectives = 3
num_verbs = 3
num_adverbs = 4
lyrics = generate_lyrics(num_nouns, num_adjectives, num_verbs, num_adverbs)
print(lyrics)
