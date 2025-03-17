import os
import datetime
import pdfplumber
import json
import hashlib


class BaseDocument:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.file_extension = os.path.splitext(file_path)[1]
    
    def get_metadata(self):
        if not os.path.exists(self.file_path):
            raise NotExistError(self.file_name)
        
        """Retrieves file metadata (size, creation date, modified date)"""
        file_size = os.path.getsize(self.file_path)
        creation_date = os.path.getctime(self.file_path) 
        file_creation_date = datetime.datetime.fromtimestamp(creation_date)
        modified_time = os.path.getmtime(self.file_path)
        file_modified_date = datetime.datetime.fromtimestamp(modified_time)
        return {
            "file_size": file_size,
            "file_creation": file_creation_date,
            "file_modification_date": file_modified_date
        }
    
    def rename(self, new_name: str):
        """Renames the document"""
        if not os.path.exists(self.file_path):
            raise NotExistError(self.file_name)
        os.rename(self.file_path, os.path.join(os.path.dirname(self.file_path), new_name))
        
    
    
    def delete(self):
        """Deletes the document"""
        if not os.path.exists(self.file_path):
            raise NotExistError(self.file_name)
        os.remove(self.file_path)


class PDFDocument(BaseDocument):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.num_pages = None  # To be determined later
    
    def extract_text(self):
        """Extracts text from PDF"""
        full_name = self.file_name + self.file_extension
        with pdfplumber.open(full_name) as file:
             text = "\n".join(page.extract_text() for page in file.pages if page.extract_text())
        return text
    
    def is_scanned(self):
        """Determines if the PDF is scanned (image-based)"""
        full_name = self.file_name + self.file_extension
        with pdfplumber.open(full_name) as file:
            has_text = False
            has_images = False
             
            for page in file.pages:
                 text = page.extract_text()
                 image = page.images #get list of images on the page
                 
                 if text and text.strip():
                     has_text = True
                 
                 if image:
                     has_images = True
            # If the PDF contains images but no text, it's likely scanned         
            if has_images:
                return True
            # If at least one page has text, it's NOT a scanned PDF
            if has_text:
                return False
         # If no text and no images, it might be an empty or metadata-only PDF   
        return False     



class TextDocument(BaseDocument):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.word_count = None
    
    def get_word_count(self):
        """Counts words in a text document"""
        if not os.path.exists(self.file_path):
            raise NotExistError(self.file_name)
        
        if self.file_extension != ".pdf":
            with open(self.file_path,"r",encoding="utf-8") as file:
                text = file.read()
                word = text.split()
                return len(word)
        elif self.file_extension == ".pdf":
            with pdfplumber.open(self.file_path) as pdf_file:
                text = "\n".join(page.extract_text() for page in pdf_file.pages if page.extract_text())
                word = text.split()
                return len(word)
        return None
    
    
    
    
    
    
class NotExistError(Exception):
    def __init__(self,file_name):
        self.file_name = file_name
        super().__init__(f"Error: the file '{file_name}' does not exist")