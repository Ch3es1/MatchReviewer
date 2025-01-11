import json
import os

# The two variables we'll use later.
team_1 = []
team_2 = []

# Get number of players on both teams,
# so we can loop through them.
player_number_team_1 = int(input("Number of players on team 1 -> "))
player_number_team_2 = int(input("Number of players on team 2 -> "))

for player in range(player_number_team_1):
    player_name = input("Player Name -> ")
    player_kills = int(input(f"{player_name}'s Kills -> "))
    player_deaths = int(input(f"{player_name}'s Deaths -> "))
    player_assists = int(input(f"{player_name}'s Assists -> "))
    player_damage = int(input(f"{player_name}'s Damage -> "))
    player_healing = int(input(f"{player_name}'s Health Healed -> "))
    player_accuracy = float(input(f"{player_name}'s Accuracy(Like 10% minus the % sign) -> "))/100
    # Easy for indexing and what not.
    temp_player = {'Name': player_name, 'Info': {'Kills': player_kills, 'Deaths': player_deaths, 'Assists': player_assists, 'Damage': player_damage, 'Healing': player_healing, 'Accuracy': player_accuracy}}
    # Adds to team_1 variable so we can calculate leaderboards and KD easier.
    team_1.append(temp_player)

# Same code copy and pasted
for player in range(player_number_team_2):
    player_name = input("Player Name -> ")
    player_kills = int(input(f"{player_name}'s Kills -> "))
    player_deaths = int(input(f"{player_name}'s Deaths -> "))
    player_assists = int(input(f"{player_name}'s Assists -> "))
    player_damage = int(input(f"{player_name}'s Damage -> "))
    player_healing = int(input(f"{player_name}'s Health Healed -> "))
    player_accuracy = float(input(f"{player_name}'s Accuracy(Like 10% minus the % sign) -> "))/100
    # Easy for indexing and what not.
    temp_player = {'Name': player_name, 'Info': {'Kills': player_kills, 'Deaths': player_deaths, 'Assists': player_assists, 'Damage': player_damage, 'Healing': player_healing, 'Accuracy': player_accuracy}}
    # Adds to team_1 variable so we can calculate leaderboards and KD easier.
    team_2.append(temp_player)

# What we'll reference for making leaderboards
team_1_leaderboard_values = {}
team_2_leaderboard_values = {}

for player in team_1:
    id = team_1.index(player)
    Kills = team_1[id]['Info']['Kills']
    Deaths = team_1[id]['Info']['Deaths']
    Assists = team_1[id]['Info']['Assists']
    Damage = team_1[id]['Info']['Damage']
    Healing = team_1[id]['Info']['Healing']
    Accuracy = team_1[id]['Info']['Accuracy']

    # Makes sure no "float division by zero" errors occur.
    if Kills == 0:
        Kills += 1
    if Deaths == 0:
        Deaths += 1
    if Damage == 0:
        Damage += 1
    if Accuracy == 0:
        Accuracy += 0.01

    # Three main things i'll make into a leaderboard.
    KD = Kills / Deaths
    KDA = (Kills+Assists) / Deaths
    Damage_Missed = (Damage/Accuracy) - Damage

    temp_leaderboard = {'Name': player['Name'], 'Info': {'Kills': Kills, 'Deaths': Deaths, 'Assists': Assists, 'Damage': Damage, 'Healing': Healing, 'Accuracy': Accuracy}, 'Values': {'KD': KD, 'KDA': KDA, 'Damage Missed': Damage_Missed}}
    team_1_leaderboard_values[f'{player['Name']}'] = temp_leaderboard

# Same code copy and pasted and tweaked
for player in team_2:
    id = team_2.index(player)
    Kills = team_2[id]['Info']['Kills']
    Deaths = team_2[id]['Info']['Deaths']
    Assists = team_2[id]['Info']['Assists']
    Damage = team_2[id]['Info']['Damage']
    Healing = team_2[id]['Info']['Healing']
    Accuracy = team_2[id]['Info']['Accuracy']

    # Makes sure no "float division by zero" errors occur.
    if Kills == 0:
        Kills += 1
    if Deaths == 0:
        Deaths += 1
    if Damage == 0:
        Damage += 1
    if Accuracy == 0:
        Accuracy += 0.01

    # Three main things i'll make into a leaderboard.
    KD = Kills / Deaths
    KDA = (Kills+Assists) / Deaths
    Damage_Missed = (Damage/Accuracy) - Damage

    temp_leaderboard = {'Name': player['Name'], 'Info': {'Kills': Kills, 'Deaths': Deaths, 'Assists': Assists, 'Damage': Damage, 'Healing': Healing, 'Accuracy': Accuracy}, 'Values': {'KD': KD, 'KDA': KDA, 'Damage Missed': Damage_Missed}}
    team_2_leaderboard_values[f'{player['Name']}'] = temp_leaderboard

if os.path.exists("Output.json"):
    os.remove("Output.json")


with open("MatchCalculator\\Output.json", "w+") as f:
    json.dump(team_1_leaderboard_values, f, indent=4)
    f.write(",\n")
    json.dump(team_2_leaderboard_values, f, indent=4)