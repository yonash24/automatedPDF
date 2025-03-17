import os
import json
import hashlib


class Database:
    def __init__(self, storage_type='json'):
        self.storage_type = storage_type
    
    def store_metadata(self, document: BaseDocument):
        """Stores document metadata in JSON/CSV/SQLite"""
        pass
    
    def retrieve_document(self, document_name: str):
        """Finds a document metadata entry"""
        pass
    
    def delete_entry(self, document_name: str):
        """Deletes a document record"""
        pass