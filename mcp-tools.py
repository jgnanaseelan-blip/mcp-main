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