""""This module handles text extraction from different document types."""

import os
import json
import hashlib
import pdfplumber


class TextExtractor:
    supported_formats = {'.pdf', '.txt'}
    
    def extract_text(self, file_path: str):
        """Extracts text from a document"""
        if self.supported_formats[0] == os.path.splitext(file_path)[1]:
            with pdfplumber.open(file_path) as pdf_file:
                text = "\n".join(page.extract_page() for page in pdf_file.pages if page.extract_text())
            return text
        elif self.supported_formats[1] == os.path.splitext(file_path)[1]:
            with open(file_path,"r") as file:
                text = file.read
            return text
    
            
    
    def search_keyword(self, text: str, keyword: str):
        """Searches for a keyword in extracted text"""
        index = 0
        count = 0
        position = []
        words = text.split()
        for word in words:
            if word == keyword:
                position[index] = count
                index += 1
            count += 1
    
    
    #require NLP skill that i need to learn
    def summarize_text(self, text: str):
        """Summarizes the extracted text"""
        pass