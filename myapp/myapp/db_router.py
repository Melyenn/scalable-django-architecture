class ReadWriteRouter:
    """
    Read/Write Splitting:
        - Master  → INSERT / UPDATE / DELETE  
        - Slave   → SELECT                   
    """

    def db_for_read(self, model, **hints):
        """Route reads to the Slave (read replica)."""
        return "replica"

    def db_for_write(self, model, **hints):
        """Route writes to the Master."""
        return "default"