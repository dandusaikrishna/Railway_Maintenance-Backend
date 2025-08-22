"""
Simple logging middleware for KPA Django project.
Logs incoming requests and outgoing responses.
"""

import time
import logging
from django.utils.deprecation import MiddlewareMixin

# Get logger
logger = logging.getLogger('django.request')

class RequestResponseLoggingMiddleware(MiddlewareMixin):
    """
    Middleware to log all incoming requests and outgoing responses.
    """
    
    def process_request(self, request):
        """Log incoming request details."""
        request.start_time = time.time()
        
        # Log basic request info
        logger.info(
            f"REQUEST || METHOD: {request.method} || PATH: {request.path} || "
            f"CLIENT_IP: {self._get_client_ip(request)} || "
            f"USER_AGENT: {request.META.get('HTTP_USER_AGENT', '')}"
        )
        
        return None
    
    def process_response(self, request, response):
        """Log outgoing response details."""
        if not hasattr(request, 'start_time'):
            return response
        
        response_time = time.time() - request.start_time
        
        logger.info(
            f"RESPONSE || METHOD: {request.method} || PATH: {request.path} || "
            f"STATUS: {response.status_code} || "
            f"TIME: {response_time:.4f}s || "
            f"CLIENT_IP: {self._get_client_ip(request)}"
        )
        
        return response
    
    def process_exception(self, request, exception):
        """Log exceptions that occur during request processing."""
        response_time = time.time() - request.start_time if hasattr(request, 'start_time') else 0
        
        logger.error(
            f"EXCEPTION || METHOD: {request.method} || PATH: {request.path} || "
            f"EXCEPTION_TYPE: {type(exception).__name__} || "
            f"EXCEPTION_MSG: {str(exception)} || "
            f"TIME: {response_time:.4f}s || "
            f"CLIENT_IP: {self._get_client_ip(request)}"
        )
        
        return None
    
    def _get_client_ip(self, request):
        """Extract client IP address from request."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
