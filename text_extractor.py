import os
import json
import hashlib


class TextExtractor:
    supported_formats = {'.pdf', '.txt'}
    
    def extract_text(self, file_path: str):
        """Extracts text from a document"""
        pass
    
    def search_keyword(self, text: str, keyword: str):
        """Searches for a keyword in extracted text"""
        pass
    
    def summarize_text(self, text: str):
        """Summarizes the extracted text"""
        pass