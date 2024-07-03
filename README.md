# Python-Project-Submission
def match_example(value):
    match value:
        case "Action":
            print("Movie: Aavesham, Leo, Rasavathi, Vikings, Kalki")
        case "Romance":
            print("Movie: After, Premam, Premalu, Hridayam, 96")
        case "Comedy":
            print("Movie: The Hangover, The Hangover 2, The Hangover 3, Dictator, Madgoan Express")
        case "Drama":
            print("Movie: The Godfather, Family Star, PT Sir, Alive, My Fault")
        case "Sci-fi":
            print("Movie: Interstellar, Civil War, Geostorm, Arrival, Passenger")
        case "Horror":
            print("Movie: Annabelle, Conjuring, Conjuring 2, Alone, Nightmare")
        case _:
            print("Please select from available Genere")

print("Enter one of the following Genre: Action, Romance, Comedy, Drama, Sci-fi, Horror ")
match_example(input("Enter the Genre: "))
