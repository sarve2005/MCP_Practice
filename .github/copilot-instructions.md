# MCP Practice Instructions

This repository is a Python MCP server built with the official MCP Python SDK and FastMCP.

- Prefer `from mcp.server.fastmcp import FastMCP` for server features.
- Keep tools, resources, and prompts type-hinted and documented with docstrings.
- Use `uv run` for local execution when available.
- Do not write diagnostic output to stdout because stdio transport uses stdout for MCP protocol messages.
- Consult the [MCP Python SDK documentation](https://py.sdk.modelcontextprotocol.io/) and [official SDK repository](https://github.com/modelcontextprotocol/python-sdk) for API details.
