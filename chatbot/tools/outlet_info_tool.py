def lookup_outlet_info(query: str) -> str:
    """Dummy tool that returns outlet data."""
    if "ss2" in query.lower():
        return "The ZUS outlet in SS2 opens at 9:00AM and is located at 5, Jalan SS 2/67, PJ."
    elif "ttdi" in query.lower():
        return "The ZUS outlet in TTDI opens at 10:00AM and is located at 88, Jalan Tun Mohd Fuad, PJ."
    else:
        return "Sorry, I couldn't find info about that outlet."