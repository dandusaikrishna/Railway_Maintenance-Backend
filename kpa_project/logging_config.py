"""
Logging configuration for KPA Django project.
Comprehensive logging with JSON formatting for better Datadog integration.
"""

import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# Create logs directory if it doesn't exist
LOG_BASE_PATH = BASE_DIR / 'logs'
LOG_BASE_PATH.mkdir(exist_ok=True)

# LOGGING CONFIGURATION
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d %(message)s"
        },
        "verbose": {
            "format": "||".join([
                "CREATED ON: %(asctime)s",
                "LEVEL: %(levelname)s",
                "LOGGER : %(name)s",
                "PATH: %(pathname)s",
                "FILE NAME: %(filename)s",
                "MODULE : %(module)s",
                "FUNCTION NAME : %(funcName)s",
                "LINE NO: %(lineno)d",
                "MESSAGE: %(message)s"
            ])
        },
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'json'  # Changed to JSON
        },
        'django.file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'json', 
            'filename': str(LOG_BASE_PATH / 'django.log'),
            'maxBytes': 10 * 1024 * 1024,  # 10 MB
            'backupCount': 5,
        },
        'requests.file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'json',
            'filename': str(LOG_BASE_PATH / 'requests.log'),
            'maxBytes': 10 * 1024 * 1024,  # 10 MB
            'backupCount': 5,
        },
        'errors.file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'json', 
            'filename': str(LOG_BASE_PATH / 'errors.log'),
            'maxBytes': 10 * 1024 * 1024,  
            'backupCount': 5,
        },
        'forms_api.file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'json',
            'filename': str(LOG_BASE_PATH / 'forms_api.log'),
            'maxBytes': 10 * 1024 * 1024,  
            'backupCount': 5,
        },
        'database.file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'json',  
            'filename': str(LOG_BASE_PATH / 'database.log'),
            'maxBytes': 10 * 1024 * 1024,  
            'backupCount': 5,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'verbose', 
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'django.file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'requests.file'],  # Added console for debugging
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console', 'requests.file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'database.file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console', 'errors.file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'forms_api': {
            'handlers': ['console', 'forms_api.file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
        'kpa_project': {
            'handlers': ['console', 'django.file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
        # Root logger - catches all unhandled logs
        '': {
            'handlers': ['console', 'errors.file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

DD_TRACE_AUTO_INSTRUMENTATION = False