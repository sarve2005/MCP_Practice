# MCP Practice

A generic Model Context Protocol server built with Python and FastMCP.

## Requirements

- Python 3.10 or newer
- `uv` recommended, or `pip`

## Run with uv

```powershell
uv sync
uv run server.py
```

For the MCP Inspector:

```powershell
uv run mcp dev server.py
```

## Run with pip

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "mcp[cli]>=1.0,<2"
python server.py
```

## Included examples

- `add`: tool that adds two integers
- `greeting://{name}`: resource template that returns a greeting
- `explain_topic`: prompt template for explaining a topic

Replace these examples with the tools, resources, and prompts for your application. Keep protocol output on stdout; send diagnostic logging to stderr.

## VS Code

The `.vscode/mcp.json` file registers the server with VS Code using the local Windows virtual environment. Open the MCP view and start `mcp-practice`, or use the MCP Inspector command above.

## Official documentation

- [MCP Python SDK](https://py.sdk.modelcontextprotocol.io/)
- [MCP Python SDK repository](https://github.com/modelcontextprotocol/python-sdk)
