import pandas as pd

__all__ = [
    "get_average_goals",
]

def get_average_goals(home, away, ignore_sides=False):
    wwmatches = pd.read_csv("../wwmatches.csv")

    avg_home = 0
    avg_away = 0
    n = 0
    
    for i in range(len(wwmatches)):
        if (home.lower() in wwmatches.iloc[i]["Home Team Name"].lower() and
            away.lower() in wwmatches.iloc[i]["Away Team Name"].lower()):
                avg_home += wwmatches.iloc[i]["Home Team Goals"]
                avg_away += wwmatches.iloc[i]["Away Team Goals"]
                n+=1
                
        if ignore_sides:
            if (home.lower() in wwmatches.iloc[i]["Away Team Name"].lower() and
                away.lower() in wwmatches.iloc[i]["Home Team Name"].lower()):
                    avg_home += wwmatches.iloc[i]["Away Team Goals"]
                    avg_away += wwmatches.iloc[i]["Home Team Goals"]
                    n+=1

    try:
        return [
            avg_home/n,
            avg_away/n
        ]
    except:
        return 0
