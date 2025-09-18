# Poly deployed @ 2025-09-18T22:17:28.185606 - demo.hello_poly - https://na1.polyapi.io/canopy/polyui/collections/server-functions/76a23874-6ff6-4900-b81e-f62979bcf3b9 - b7c9bcf
from polyapi.typedefs import PolyServerFunction


polyConfig: PolyServerFunction = {
    "name": "hello_poly",
    "context": "demo",
}


def hello_poly(first_name: str, last_name: str) -> str:
    """Greet new users of Poly

    Args:
        first_name (str): The user's first name
        last_name (str): 

    Returns:
        str: A greeting for the user from Poly
    """
    return f"Hello {first_name} of House {last_name}! I'm Poly, your helpful guide to the world of api integrations and middleware."
