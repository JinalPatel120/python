import random


def select_team(match,previous_team):
    available_team=[team for team in match if team not in previous_team]
    if len(available_team) <2:
        available_team=match
    return random.sample(available_team,2)

teams=['team1','team2','team3','team4','team5','team6','team7','team8']
previous_team=[]

for day in range(1,len(teams)):
    match=select_team(teams,previous_team)
    print(match)