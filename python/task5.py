from typing import List, Tuple
from datetime import datetime, timedelta
import random
import re 

class Team:
    def __init__(self, name: str):
        """
        Initialize a Team instance.

        :param name: The name of the team.
        """
        self.name = name


class Tournament:
    def __init__(self):
        """
        Initialize a Tournament instance with an empty list of teams and an empty schedule.
        """
        self.teams: List[Team] = []
        self.schedule: List[Tuple[str, str, str, str]] = []  # Added venue to schedule
        self.venues: List[str] = []  # List of venues

    def register_team(self, team_name: str) -> None:
        """
        Register a team in the tournament.

        :param team_name: The name of the team to register.
        :raises ValueError: If the team name is empty or contains special characters.
        """
        if not team_name.strip() or not re.match(r'^[a-zA-Z0-9\s]+$', team_name):
            raise ValueError("Team name cannot be empty and must contain only alphanumeric characters and spaces.")
        
        self.teams.append(Team(team_name))

    def add_venue(self, venue_name: str) -> None:
        """
        Add a venue to the tournament.

        :param venue_name: The name of the venue to add.
        :raises ValueError: If the venue name is empty or contains special characters.
        """
        if not venue_name.strip() or not re.match(r'^[a-zA-Z0-9\s]+$', venue_name):
            raise ValueError("Venue name cannot be empty and must contain only alphanumeric characters and spaces.")
        
        self.venues.append(venue_name)

    def generate_schedule(self) -> None:
        """
        Generate the tournament schedule.

        :raises ValueError: If there are fewer than two teams or not enough venues registered.
        """
        if len(self.teams) < 2:
            raise ValueError("At least two teams are required to generate a schedule.")
        if len(self.venues) < len(self.teams) // 2:  
            raise ValueError("At least one venue is required for every pair of teams.")

        num_teams = len(self.teams)
        self.schedule = self.create_fixture(num_teams)

    def create_fixture(self, num_teams: int) -> List[Tuple[str, str, str, str]]:
        """
        Create a randomized fixture for the tournament.

        :param num_teams: The number of teams participating in the tournament.
        :return: A list of match fixtures as tuples of match date, teams, and venue.
        """
        fixtures = []
        start_date = datetime.now()

        for i in range(num_teams):
            for j in range(num_teams):
                if i != j:
                    fixtures.append((self.teams[i].name, self.teams[j].name))

        random.shuffle(fixtures)
        print(len(fixtures),'length')
      
        schedule = []
        last_opponent = {team.name: None for team in self.teams}
        print(last_opponent,'last opponent')
        match_today = fixtures.pop(0)
        schedule.append(match_today)
        count=0
        # while schedule.__len__()!=fixtures.__len__():
        #     a,b=schedule[count]
        #     for item in fixtures:   
        #         x,y=item     
        #         if a==x or b==y or a==y or b==x:
        #             continue
        #         else:

        #             schedule.append(item)
        #             fixtures.remove(item)
        #             count+=1
        #             break

        # for item in schedule:
        #     x,y=item     
        #     match_date = start_date + timedelta(days=len(schedule))
        #     venue = random.choice(self.venues) 
        #     schedule.append((match_date.strftime("%Y-%m-%d"), x, y, venue))   
        # print(schedule,'schedule')

        while fixtures:
            count+=1
            match_today = fixtures.pop(0)
            print(match_today)
            team1, team2 = match_today
       
     
            if (last_opponent[team1] == team2) or (last_opponent[team2] == team1):
                    fixtures.append(match_today)
                    continue
            
            match_date = start_date + timedelta(days=len(schedule))
            venue = random.choice(self.venues) 
            schedule.append((match_date.strftime("%Y-%m-%d"), team1, team2, venue))

            last_opponent[team1] = team2
            last_opponent[team2] = team1

        print('counter',count)
        return schedule
        

    def display_schedule(self) -> None:
        """
        Display the tournament schedule.
        """
        if not self.schedule:
            print("Schedule not generated yet.")
            return
        print("Tournament Schedule:")
        for date, team1, team2, venue in self.schedule:
            print(f"{date}: {team1} vs {team2} at {venue}")

def main():
    tournament = Tournament()

    # Register teams
    while True:
        team_name = input("Enter team name (or 'done' to finish registration): ")
        if team_name.lower() == 'done':
            break
        try:
            tournament.register_team(team_name)
            print(f"Team '{team_name}' registered successfully.")
        except ValueError as e:
            print(f"Error: {e}") 

    # Register venues
    while True:
        venue_name = input("Enter venue name (or 'done' to finish registration): ")
        if venue_name.lower() == 'done':
            break
        try:
            tournament.add_venue(venue_name)
            print(f"Venue '{venue_name}' added successfully.")
        except ValueError as e:
            print(f"Error: {e}")  
    tournament.generate_schedule()
    # try:
    #     tournament.generate_schedule()
    #     print("Fixture generated successfully.")
    # except ValueError as e:
    #     print(f"Error: {e}")  

    # Display schedule
    while True:
        print("\nMenu:")
        print("1. Display schedule")
        print("2. Exit")
        
        choice = input("Select an option (1-2): ")
        if choice == '1':
            tournament.display_schedule()
        elif choice == '2':
            print("Exiting the tournament management system.")
            break
        else:
            print("Invalid option, please select 1 or 2.")  

if __name__ == "__main__":
    main()


# def create_fixture(self, num_teams: int) -> List[Tuple[str, str, str, str]]:
#         """
#         Create a randomized fixture for the tournament.

#         :param num_teams: The number of teams participating in the tournament.
#         :return: A list of match fixtures as tuples of match date, teams, and venue.
#         """
#         fixtures = []
#         start_date = datetime.now()

#         for i in range(num_teams):
#             for j in range(num_teams):
#                 if i != j:
#                     fixtures.append((self.teams[i].name, self.teams[j].name))

 
#         print(len(fixtures),'length')
      
#         schedule = []
#         last_opponent = {team.name: None for team in self.teams}
#         print(last_opponent,'last opponent')
#         match_today = fixtures.pop(0)
#         schedule.append(match_today)
#         count=0
#         while_counter=0
#         for_counter=0
#         while schedule.__len__()!=fixtures.__len__():
#             while_counter+=1
#             team1,team2=schedule[count]
#             for item in fixtures: 
#                 for_counter+=1  

#                 x,y=item     
#                 if team1==x or team2==y or team1==y or team2==x:
#                     continue
#                 else:
#                     schedule.append(item)
#                     fixtures.remove(item)
#                     count+=1
#                     break
        
#         print(for_counter,'for counter')
#         print(while_counter,'while counter')

#         new_schedule=[]
#         for item in schedule:
#             print(item,'item')
#             x,y=item     
#             match_date = start_date + timedelta(days=len(schedule))
#             venue = random.choice(self.venues) 
#             new_schedule.append((match_date.strftime("%Y-%m-%d"), x, y, venue))   
#         print(schedule,'schedule')

#         return new_schedule