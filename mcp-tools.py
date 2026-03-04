import logging
from chuk_mcp_runtime import mcp_tool

log = logging.getLogger(__name__)

@mcp_tool(name="add_numbers")
async def add_numbers(a: float, b: float):
    """
    Add two numbers and return the result.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        result (float): Sum of the two numbers
    """

    log.info(f"Calling add_numbers tool with values: a={a}, b={b}")

    result = a + b

    response = {
        "a": a,
        "b": b,
        "result": result
    }

    log.info(f"Response of add_numbers tool: {response}")

    return response
    
@mcp_tool(name="say_hi")
async def say_hi(name: str = "User"):
    """
    Return a greeting message.

    Args:
        name (str): Name of the person to greet

    Returns:
        message (str): Greeting message
    """

    log.info(f"Calling say_hi tool with name: {name}")

    message = f"Hi {name}! Welcome to the MCP server."

    response = {
        "name": name,
        "message": message
    }

    log.info(f"Response of say_hi tool: {response}")

    return response
