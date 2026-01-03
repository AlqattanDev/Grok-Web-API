"""Constants and configuration for Grok Web API."""

from enum import Enum


class GrokEndpoints:
    """Grok API endpoints."""
    BASE_URL = "https://grok.com"
    API_BASE = "https://grok.com/api"
    
    # Image generation endpoints
    IMAGINE_SESSION = f"{API_BASE}/imagine/session"
    IMAGINE_GENERATE = f"{API_BASE}/imagine/generate"
    IMAGINE_IMAGE = f"{API_BASE}/imagine/{{image_id}}"
    IMAGINE_VARIATIONS = f"{API_BASE}/imagine/{{image_id}}/variations"
    IMAGINE_MODIFY = f"{API_BASE}/imagine/{{image_id}}/modify"
    
    # Auth endpoints
    AUTH_CHECK = f"{API_BASE}/user/auth"
    AUTH_REFRESH = f"{API_BASE}/auth/refresh"
    
    # Web URLs
    IMAGINE_WEB = f"{BASE_URL}/imagine"
    LOGIN = f"{BASE_URL}/login"


class ImageQuality(str, Enum):
    """Image quality options."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    ULTRA = "ultra"


class ImageSize(str, Enum):
    """Supported image sizes."""
    SQUARE = "1:1"
    PORTRAIT = "9:16"
    LANDSCAPE = "16:9"
    TALL = "4:3"
    WIDE = "3:4"


class ImageStyle(str, Enum):
    """Predefined image styles."""
    REALISTIC = "realistic"
    ANIME = "anime"
    OIL_PAINTING = "oil_painting"
    WATERCOLOR = "watercolor"
    SKETCH = "sketch"
    CYBERPUNK = "cyberpunk"
    FANTASY = "fantasy"
    SCIFI = "sci-fi"


# Request configuration
DEFAULT_TIMEOUT = 30
DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_DELAY = 1  # seconds

# Rate limiting
REQUESTS_PER_MINUTE = 10
IMAGES_PER_DAY = 100

# Browser configuration
BROWSER_TIMEOUT = 30000  # milliseconds
BROWSER_HEADLESS = True

# Cookie configuration
COOKIE_REFRESH_INTERVAL = 3600  # 1 hour in seconds
