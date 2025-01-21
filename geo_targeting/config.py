"""
Geographic targeting configuration for LA Fitness Warren lead generation system.
"""

# Warren, MI coordinates (approximate center)
WARREN_CENTER = {
    'latitude': 42.4775,
    'longitude': -83.0277
}

# Target radius in miles
TARGET_RADIUS = 10

# Warren and surrounding area zip codes
TARGET_ZIP_CODES = [
    '48088',  # Warren
    '48089',  # Warren
    '48091',  # Warren
    '48092',  # Warren
    '48093',  # Warren
    '48397',  # Warren
    '48090',  # Warren
    # Surrounding areas will be dynamically calculated
]

# API Configuration
MAPS_API_CONFIG = {
    'api_key': None,  # To be configured
    'requests_per_second': 10,
    'cache_duration': 86400  # 24 hours in seconds
}