from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app_key = os.getenv("APP_KEY")
api_token = os.getenv("API_TOKEN")
base_url = os.getenv("BASE_URL")
host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", "10000"))
transport = os.getenv("MCP_TRANSPORT", "stdio")

auth_query = {
    "key":app_key,
    "token":api_token
}

mcp = FastMCP("MCP Practice", host=host, port=port)

@mcp.tool()
def create_board(name: str) -> str:
    """Create a new Trello board.

    Args:
        name: The name to assign to the new board.

    Returns:
        The Trello API response containing the created board details.
    """
    url = base_url + "boards/"
    query = {
        "name":name
    }
    query = query | auth_query
    response = requests.request(
        "POST",
        url,
        params=query
    )
    return response.text

@mcp.tool()
def delete_board(id:str) -> str:
    """Delete a Trello board.

    Args:
        id: The Trello board ID to delete.

    Returns:
        The Trello API response confirming the deletion.
    """
    url = base_url + f"boards/{id}"
    query = auth_query
    response = requests.request(
        "DELETE",
        url,
        params=query
    )
    return response.text

@mcp.tool()
def create_list(name:str,idBoard:str) -> str:
    """Create a new list on a Trello board.

    Args:
        name: The name to assign to the new list.
        idBoard: The Trello board ID where the list will be created.

    Returns:
        The Trello API response containing the created list details.
    """
    url = base_url + "lists"
    query = {
        "name":name,
        "idBoard":idBoard
    }

    query = query|auth_query
    response = requests.request(
        "POST",
        url,
        params=query
    )
    return response.text
    

@mcp.tool()
def create_card(name: str, idList: str) -> str:
    """Create a new card in a Trello list.

    Args:
        name: The name to assign to the new card.
        idList: The Trello list ID where the card will be created.

    Returns:
        The Trello API response containing the created card details.
    """
    url = base_url + "cards"
    query = {
        "name": name,
        "idList":idList
    }
    query = query|auth_query
    response = requests.request(
        "POST",
        url,
        params=query
    )
    return response.text

@mcp.tool()
def delete_card(id:str) -> str:
    """Delete a Trello card.

    Args:
        id: The Trello card ID to delete.

    Returns:
        The Trello API response confirming the deletion.
    """
    url = base_url + f"cards/{id}"
    query = auth_query
    response = requests.request(
        "DELETE",
        url,
        params=query
    )
    return response.text

@mcp.tool()
def search(query:str,cards_limit:int = 5,boards_limit:int = 5) -> str:
    """Search Trello cards and boards by text.

    Args:
        query: The text to search for across cards and boards.
        cards_limit: The maximum number of cards to return.
        boards_limit: The maximum number of boards to return.

    Returns:
        The Trello API response containing matching cards and boards.
    """
    url = base_url + "search"
    query = {
        "query":query,
        "modelTypes":"cards,boards",# the api can return members and workspace entity too , so here i am restricting to cards and boards alone
        "cards_limit":cards_limit,
        "boards_limit":boards_limit
    }
    query = query | auth_query
    response = requests.request(
        "GET",
        url,
        params=query
    )
    return response.text

@mcp.resource("boards://all")
def get_boards() -> str:
    """Retrieve all Trello boards available to the authenticated user.

    Returns:
        The Trello API response containing the user's boards.
    """
    url = base_url + "members/me/boards"
    query = auth_query
    response = requests.request(
        "GET",
        url,
        params=query
    )
    return response.text

@mcp.resource("boards://{id}")
def get_board(id: str) -> str:
    """Retrieve details for one Trello board.

    Args:
        id: The Trello board ID to retrieve.

    Returns:
        The Trello API response containing the board details.
    """
    url = base_url + f"boards/{id}"
    query = auth_query
    response = requests.request(
        "GET",
        url,
        params=query
    )
    return response.text

@mcp.resource("boards://{idBoard}/lists")
def get_lists(idBoard: str) -> str:
    """Retrieve all lists belonging to a Trello board.

    Args:
        idBoard: The Trello board ID whose lists should be retrieved.

    Returns:
        The Trello API response containing the board's lists.
    """
    url = base_url + f"boards/{idBoard}/lists"
    query = auth_query
    response = requests.request(
        "GET",
        url,
        params=query
    )
    return response.text

@mcp.resource("lists://{id}")
def get_list(id: str) -> str:
    """Retrieve details for one Trello list.

    Args:
        id: The Trello list ID to retrieve.

    Returns:
        The Trello API response containing the list details.
    """
    url = base_url + f"lists/{id}"
    query = auth_query
    response = requests.request(
        "GET",
        url,
        params=query
    )
    return response.text

@mcp.resource("boards://{idBoard}/cards")
def get_cards(idBoard: str) -> str:
    """Retrieve all cards belonging to a Trello board.

    Args:
        idBoard: The Trello board ID whose cards should be retrieved.

    Returns:
        The Trello API response containing the board's cards.
    """
    url = base_url + f"boards/{idBoard}/cards"
    query = auth_query
    response = requests.request(
        "GET",
        url,
        params=query
    )
    return response.text

@mcp.resource("cards://{id}")
def get_card(id: str) -> str:
    """Retrieve details for one Trello card.

    Args:
        id: The Trello card ID to retrieve.

    Returns:
        The Trello API response containing the card details.
    """
    url = base_url + f"cards/{id}"
    query = auth_query
    response = requests.request(
        "GET",
        url,
        params=query
    )
    return response.text



@mcp.prompt()
def trello_prompt(topic: str) -> str:
    """Create a focused system prompt for a Trello assistant.

    Args:
        topic: The user's Trello request or task.

    Returns:
        A prompt that guides the LLM to handle the Trello request safely.
    """
    return f"""You are a helpful Trello assistant.

Your task is to help the user manage Trello boards, lists, and cards. Use the
available Trello tools and resources when the request requires reading or
changing Trello data.

Follow these rules:
- Identify the requested action before using a tool.
- Use the correct board, list, or card ID when one is provided.
- Ask a concise clarification question when a required ID or name is missing.
- Never claim that an action succeeded unless the tool response confirms it.
- Summarize the result clearly and mention any relevant Trello IDs.
- Do not expose API keys, tokens, or other credentials.

User request:
{topic}
"""


if __name__ == "__main__":
    mcp.run(transport=transport)
