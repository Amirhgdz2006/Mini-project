import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

def load_users(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def create_leaderboard(users):
    sorted_users = sorted(users, key=lambda x: x.get('score', 0), reverse=True)
    return sorted_users
def display_leaderboard(leaderboard):
    console = Console()

    print('\n')
    
    khode_leaderboard = Table(title="", title_justify="center")
    khode_leaderboard.add_column("RANK", justify="center", style="cyan", no_wrap=True)
    khode_leaderboard.add_column("USERNAME", justify="left", style="royal_blue1")
    khode_leaderboard.add_column("SCORE", justify="right", style="spring_green4")  
    khode_leaderboard.add_column("WINS", justify="right", style="bright_magenta")
    khode_leaderboard.add_column("LOSSES", justify="right", style="red")

    for index, user in enumerate(leaderboard):
        khode_leaderboard.add_row(
            str(index + 1),
            user['username'],
            str(user.get('score', 0)),
            str(user.get('wins', 0)),
            str(user.get('losses', 0))
        )
    
    console.print(khode_leaderboard)

    print('\n')
def main():
    file_name = 'users.json'
    users = load_users(file_name)
    leaderboard = create_leaderboard(users)
    display_leaderboard(leaderboard)

if __name__ == '__main__':
    main()
