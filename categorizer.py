import os
import json
import hashlib


class DocumentCategorizer:
    categories = {
        "invoice": {"invoice", "bill", "amount due"},
        "report": {"report", "summary", "analysis"},
        "contract": {"agreement", "contract", "terms"},
    }
    
    def categorize_document(self, text: str):
        """Determines the category of a document based on keywords"""
        pass
    
    def add_category(self, category_name: str, keyword_list: set):
        """Adds a new document category"""
        pass
    
    def remove_category(self, category_name: str):
        """Removes a document category"""
        pass