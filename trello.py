import requests
import sys
from dotenv import load_dotenv
import os
# Constants


load_dotenv()  # This loads the environment variables from .env

# Constants
API_KEY = os.getenv('TRELLO_API_KEY')
TOKEN = os.getenv('TRELLO_TOKEN')
BASE_URL = 'https://api.trello.com/1/'


def create_card(board_id, list_id, card_name, card_desc, labels, comment):
    url = f"{BASE_URL}cards"
    query = {
        'key': API_KEY,
        'token': TOKEN,
        'idList': list_id,
        'name': card_name,
        'desc': card_desc,
        'idLabels': labels
    }
    response = requests.post(url, params=query)
    card = response.json()

    # Add comment to the card
    if comment:
        comment_url = f"{BASE_URL}cards/{card['id']}/actions/comments"
        comment_query = {
            'key': API_KEY,
            'token': TOKEN,
            'text': comment
        }
        requests.post(comment_url, params=comment_query)

    return card

def main():
    if len(sys.argv) < 6:
        print("Usage: python trello_cli.py <board_id> <list_id> <card_name> <card_desc> <labels_comma_separated> [comment]")
        sys.exit(1)

    board_id = sys.argv[1]
    list_id = sys.argv[2]
    card_name = sys.argv[3]
    card_desc = sys.argv[4]
    labels = sys.argv[5].split(',')
    comment = sys.argv[6] if len(sys.argv) > 6 else ''

    card = create_card(board_id, list_id, card_name, card_desc, labels, comment)
    print(f"Card created successfully. Card ID: {card['id']}")

if __name__ == "__main__":
    main()
