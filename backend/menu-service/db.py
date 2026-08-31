"""
db.py — PostgreSQL connection helper for the menu-service.

Connection details come from the DATABASE_URL environment variable.
When running inside Docker, DATABASE_URL should point to the Windows host
using host.docker.internal.
"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor


DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:postgres@172.25.80.1:5432/flavorblitz",
)


def get_connection():
    """Open a connection to PostgreSQL."""
    return psycopg2.connect(
        DATABASE_URL,
        cursor_factory=RealDictCursor,
    )