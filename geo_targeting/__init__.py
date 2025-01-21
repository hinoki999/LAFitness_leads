"""
Geographic targeting module for LA Fitness Warren lead generation system.
"""

from .geo_utils import calculate_distance, is_within_radius, validate_zip_code
from .config import WARREN_CENTER, TARGET_RADIUS, TARGET_ZIP_CODES, MAPS_API_CONFIG

__all__ = [
    'calculate_distance',
    'is_within_radius',
    'validate_zip_code',
    'WARREN_CENTER',
    'TARGET_RADIUS',
    'TARGET_ZIP_CODES',
    'MAPS_API_CONFIG'
]