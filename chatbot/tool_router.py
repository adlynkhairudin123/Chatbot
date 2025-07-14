# from tools.outlet_info_tool import lookup_outlet_info
# import re

# def route_tool_call(tool_string: str) -> str:
#     """Decodes the tool action string and calls the correct tool."""
#     # Normalize and clean the tool string
#     tool_string = tool_string.strip()

#     # Match and extract outlet name from correct format
#     match = re.match(r"lookup_outlet_info\s*:\s*([^\(\n]+)", tool_string, re.IGNORECASE)
#     if match:
#         outlet_name = match.group(1).strip()
#         return lookup_outlet_info(outlet_name)

#     return "(Tool not recognized or format incorrect.)"

from tools.outlet_info_tool import lookup_outlet_info
from tools.calculator_tool import safe_calculate 

def route_tool_call(tool_string: str) -> str:
    if tool_string.lower().startswith("lookup_outlet_info"):
        query = tool_string.split(":", 1)[1] if ":" in tool_string else ""
        return lookup_outlet_info(query)

    elif tool_string.lower().startswith("calculator"):
        expr = tool_string.split(":", 1)[1] if ":" in tool_string else ""
        return safe_calculate(expr)

    return "(Tool not recognized.)"
