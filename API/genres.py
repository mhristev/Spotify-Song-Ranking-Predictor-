genre_classification = {
    "Pop": ['gen z singer-songwriter', 'viral pop', 'pop nacional', 'pop rap', 'uk pop', 'canadian pop', 'dance pop', 'italian pop', 'funk pop', 'pop reggaeton', 'classic uk pop', 'bedroom pop', 'italian adult pop', 'brill building pop', 'sertanejo pop', 'art pop', 'colombian pop', 'pop venezolano', 'new wave pop', 'latin pop', 'post-teen pop', 'europop', 'australian pop', 'singer-songwriter pop'],
    "Rock": ['rock', 'rock-and-roll', 'folk punk', 'psychedelic rock', 'garage rock', 'heartland rock', 'soft rock', 'sheffield indie', 'modern alternative rock', 'modern rock', 'album rock', 'permanent wave', 'folk rock'],
    "Electronic/Dance": ['brostep', 'electro house', 'experimental', 'slap house', 'electronic trap', 'edm', 'trance', 'filter house', 'uk dance', 'funk carioca', 'electro', 'progressive house', 'australian dance', 'big room', 'dutch edm', 'house', 'progressive electro house'],
    "Rap/Hip Hop": ['dirty south rap', 'italian hip hop', 'ohio hip hop', 'trap soul', 'taiwan hip hop', 'melodic rap', 'argentine hip hop', 'queens hip hop', 'chicago rap', 'gangster rap', 'atl trap', 'uk hip hop', 'rap napoletano', 'rage rap', 'west coast rap', 'r&drill', 'north carolina hip hop', 'australian hip hop', 'underground hip hop', 'hip hop', 'atl hip hop', 'latin hip hop', 'plugg', 'pluggnb', 'kentucky hip hop', 'chicago drill', 'drill', 'deep underground hip hop', 'indie hip hop', 'trap argentino', 'old school atlanta hip hop', 'rap canario'],
    "Reggaeton/Latin": ['reggaeton flow', 'trap italiana', 'reggaeton chileno', 'southern hip hop', 'urbano latino', 'reggaeton', 'mambo chileno', 'musica mexicana', 'trap latino', 'reggaeton colombiano'],
    "Country/Folk": ['southern soul', 'stomp and holler', 'american folk revival', 'modern country rock', 'folk punk', 'classic oklahoma country', 'indie folk', 'classic texas country', 'western swing'],
    "R&B/Soul": ['trap soul', 'uk contemporary r&b', 'contemporary r&b', 'indie r&b', 'bedroom soul', 'alternative r&b', 'r&b', 'neo soul', 'urban contemporary', 'chicago soul'],
    "Blues/Jazz": ['blues', 'motown', 'swing', 'blues rock'],
    "World": ['barbadian pop', 'southern soul', 'samba reggae', 'k-pop', 'rockabilly', 'banda', 'celtic punk', 'afrobeats', 'video game music', 'puerto rican pop', 'j-division', 'desi pop', 'nigerian pop', 'celtic rock']
}

genre_classification["Pop"].extend(['bedroom pop', 'italian adult pop', 'brill building pop', 'sertanejo pop', 'art pop', 'colombian pop', 'pop venezolano', 'new wave pop', 'latin pop', 'post-teen pop', 'europop'])
genre_classification["Rock"].extend(['sheffield indie', 'modern alternative rock', 'modern rock'])
genre_classification["Electronic/Dance"].extend(['progressive house', 'australian dance', 'big room', 'dutch edm'])
genre_classification["Rap/Hip Hop"].extend(['rage rap', 'west coast rap', 'r&drill', 'north carolina hip hop', 'australian hip hop', 'underground hip hop', 'hip hop', 'atl hip hop', 'latin hip hop', 'plugg'])
genre_classification["Reggaeton/Latin"].extend(['mambo chileno', 'musica mexicana', 'arrocha', 'agronejo', 'sierreno', 'latin pop', 'trap latino', 'latin hip hop'])
genre_classification["Country/Folk"].extend(['classic oklahoma country', 'indie folk'])
genre_classification["R&B/Soul"].extend(['bedroom soul', 'alternative r&b', 'r&b', 'quiet storm'])
genre_classification["Blues/Jazz"].extend(['torch song'])
genre_classification["World"].extend(['musical advocacy', 'afrobeats', 'new romantic', 'video game music', 'talent show', 'mellow gold', 'axe', 'filmi', 'puerto rican pop', 'j-division', 'europop'])

genre_classification["Pop"].extend(['aussietronica', 'australian pop', 'folk-pop', 'singer-songwriter pop'])
genre_classification["Rock"].extend(['album rock', 'permanent wave'])
genre_classification["Electronic/Dance"].extend(['pluggnb', 'house', 'progressive electro house', 'moombahton', 'float house'])
genre_classification["Rap/Hip Hop"].extend(['kentucky hip hop', 'chicago drill', 'drill', 'deep underground hip hop', 'indie hip hop', 'trap argentino', 'rap canario'])
genre_classification["Reggaeton/Latin"].extend(['pagode', 'pagode baiano', 'reggaeton colombiano', 'funk rj'])
genre_classification["Country/Folk"].extend(['country', 'folk rock', 'contemporary country', 'western swing', 'classic texas country'])
genre_classification["R&B/Soul"].extend(['neo soul', 'urban contemporary', 'chicago soul'])
genre_classification["Blues/Jazz"].extend(['lounge', 'deep adult standards'])
genre_classification["World"].extend(['halloween', 'modern bollywood', 'desi pop', 'nigerian pop', 'new wave', 'singer-songwriter', 'speedrun', 'celtic rock', 'old school atlanta hip hop'])

genre_classification["Pop"].extend(['australian electropop', 'hip pop', 'classic girl group', 'pov: indie', 'pop dance', 'baroque pop', 'sophisti-pop', 'psychedelic pop', 'canadian contemporary r&b', 'chill pop', 'pop', 'synthpop', 'sunshine pop'])
genre_classification["Rock"].extend(['glam rock', 'alternative dance', 'piano rock'])
genre_classification["Electronic/Dance"].extend(['electra', 'hypertechno'])
genre_classification["Rap/Hip Hop"].extend(['houston rap', 'south carolina hip hop', 'rap', 'urbano chileno', 'canadian hip hop', 'viral rap', 'conscious hip hop', 'indie pop rap'])
genre_classification["Reggaeton/Latin"].extend(['corridos tumbados'])
genre_classification["Country/Folk"].extend(['country road', 'traditional country', 'country dawn'])
genre_classification["R&B/Soul"].extend(['soul', 'easy listening', 'vocal jazz', 'jazz pop', 'classic soul'])
genre_classification["Blues/Jazz"].extend([])
genre_classification["World"].extend(['yodeling', 'k-pop boy group', 'mandopop', 'brooklyn indie', 'mpb', 'novelty', 'sertanejo'])

genre_classification["Pop"].extend(['boy band', 'korean ost', 'irish singer-songwriter'])
genre_classification["Rock"].extend(['classic rock', 'punk', 'yacht rock'])
genre_classification["Electronic/Dance"].extend(['trap queen', 'experimental pop'])
genre_classification["Rap/Hip Hop"].extend(['trap', 'melodic drill', 'crunk'])
genre_classification["Reggaeton/Latin"].extend(['corrido', 'norteno', 'musica chihuahuense', 'sad sierreno', 'sertanejo universitario'])
genre_classification["Country/Folk"].extend(['cowboy western'])
genre_classification["R&B/Soul"].extend(['adult standards'])
genre_classification["Blues/Jazz"].extend(['light music'])
genre_classification["World"].extend(['funk', 'merseybeat', 'british invasion'])
genre_classification["Pop"].extend(['vocal harmony group', 'a cappella'])
genre_classification["Rock"].extend(['man\'s orchestra'])

genre_classification["Rap/Hip Hop"].extend(['dfw rap', 'futuristic swag', 'battle rap', 'harlem hip hop', 'east coast hip hop', 'sudanese hip hop'])
genre_classification["Pop"].extend(['alt z', 'modern country pop', 'classic italian pop', 'sudanese pop'])
genre_classification["Country/Folk"].extend(['black americana', 'nashville sound', 'outlaw country', 'country rock', 'classic country pop'])
genre_classification["Rock"].extend(['swamp rock', 'modern folk rock'])

genre_classification["Rap/Hip Hop"].append('k-rap')
genre_classification["R&B/Soul"].append('korean r&b')
genre_classification["Pop"].extend(['korean pop', 'turkish pop'])

def categorize_genre(genre):
    for category, genres_in_category in genre_classification.items():
        if genre in genres_in_category:
            return category
    print(genre)
    return 'Miscellaneous/Unique'

