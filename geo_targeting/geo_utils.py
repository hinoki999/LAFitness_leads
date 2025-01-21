"""
Utility functions for geographic calculations and validations.
"""
import math
from typing import Dict, List, Tuple

def calculate_distance(point1: Dict[str, float], point2: Dict[str, float]) -> float:
    """
    Calculate the distance between two points using the Haversine formula.
    
    Args:
        point1: Dict with 'latitude' and 'longitude' keys
        point2: Dict with 'latitude' and 'longitude' keys
        
    Returns:
        Distance in miles
    """
    R = 3959.87433  # Earth's radius in miles

    lat1 = math.radians(point1['latitude'])
    lon1 = math.radians(point1['longitude'])
    lat2 = math.radians(point2['latitude'])
    lon2 = math.radians(point2['longitude'])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c

def is_within_radius(target: Dict[str, float], point: Dict[str, float], radius: float) -> bool:
    """
    Check if a point is within the specified radius of the target.
    
    Args:
        target: Dict with target 'latitude' and 'longitude'
        point: Dict with point 'latitude' and 'longitude'
        radius: Maximum distance in miles
        
    Returns:
        Boolean indicating if point is within radius
    """
    return calculate_distance(target, point) <= radius

def validate_zip_code(zip_code: str) -> bool:
    """
    Validate if a zip code is properly formatted.
    
    Args:
        zip_code: String representation of zip code
        
    Returns:
        Boolean indicating if zip code is valid
    """
    return len(zip_code) == 5 and zip_code.isdigit()