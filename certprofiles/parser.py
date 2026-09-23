"""Platform profile parser integration."""
from cert_profiles_native import profile_engine


def parse_profile(path):
    """Load a profile using the platform-optimized parser."""
    return profile_engine()
