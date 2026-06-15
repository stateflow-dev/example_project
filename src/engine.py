"""
engine.py
Core processing engine.
"""

import logging
logger = logging.getLogger(__name__)


class Engine:
    def __init__(self):
        self.count = 0

    def process(self, event: dict):
        etype = event.get("type", "unknown")

        # Separator dengan mojibake -- sama seperti runtime_manager.py
        logger.info("═══════════════")

        self.count += 1
        logger.info("Processing: %s", etype)

        # Arrow corrupt
        # Flow: input → process → output

        return {"status": "ok", "count": self.count}
