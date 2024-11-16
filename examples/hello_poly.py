from polyapi.typedefs import PolyServerFunction

polyConfig: PolyServerFunction = {
    "name": "hello_poly",
    "context": "demo",
}

def hello_poly(first_name: str) -> str:
    """Greet new users of Poly

    Args:
        first_name (str): The user's first name

    Returns:
        str: A greeting for the user from Poly
    """
    return f"Hello {first_name}! I'm Poly, your helpful guide to the world of api integrations and middleware."
