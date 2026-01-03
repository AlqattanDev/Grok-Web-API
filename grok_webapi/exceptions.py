"""Exception classes for Grok Web API."""


class GrokError(Exception):
    """Base exception for all Grok API errors."""
    pass


class GrokAuthenticationError(GrokError):
    """Raised when authentication fails or cookies are invalid."""
    pass


class GrokGenerationError(GrokError):
    """Raised when image generation fails."""
    pass


class GrokNetworkError(GrokError):
    """Raised when network request fails."""
    pass


class GrokRateLimitError(GrokError):
    """Raised when rate limit is exceeded."""
    pass


class GrokTimeoutError(GrokError):
    """Raised when request times out."""
    pass


class GrokSessionError(GrokError):
    """Raised when session-related operations fail."""
    pass
