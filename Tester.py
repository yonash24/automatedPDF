import unittest
import os
import tempfile
from document_handler import BaseDocument, PDFDocument, TextDocument, NotExistError  # Assuming the script is saved as document_handler.py

class TestBaseDocument(unittest.TestCase):
    def setUp(self):
        # Create a temporary file
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.file_path = self.temp_file.name
        self.document = BaseDocument(self.file_path)
        
    def tearDown(self):
        # Remove the temporary file
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_get_metadata(self):
        metadata = self.document.get_metadata()
        self.assertIn("file_size", metadata)
        self.assertIn("file_creation", metadata)
        self.assertIn("file_modification_date", metadata)
    
    def test_rename(self):
        new_name = self.file_path + "_renamed"
        self.document.rename(new_name)
        self.assertTrue(os.path.exists(new_name))
        os.rename(new_name, self.file_path)  # Rename back for cleanup
    
    def test_delete(self):
        self.document.delete()
        self.assertFalse(os.path.exists(self.file_path))

    def test_non_existent_file(self):
        os.remove(self.file_path)
        with self.assertRaises(NotExistError):
            self.document.get_metadata()


class TestTextDocument(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8')
        self.temp_file.write("Hello world! This is a test document.")
        self.temp_file.close()
        self.document = TextDocument(self.temp_file.name)
    
    def tearDown(self):
        try:
            os.remove(self.temp_file.name)
        except FileNotFoundError:
            pass
    
    def test_get_word_count(self):
        word_count = self.document.get_word_count()
        self.assertEqual(word_count, 6)


class TestPDFDocument(unittest.TestCase):
    def setUp(self):
        # Create a dummy PDF file
        self.temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        self.file_path = self.temp_pdf.name
        self.temp_pdf.close()
        self.document = PDFDocument(self.file_path)
    
    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
    
    def test_extract_text_empty_pdf(self):
        text = self.document.extract_text()
        self.assertEqual(text, "")
    
    def test_is_scanned_empty_pdf(self):
        self.assertFalse(self.document.is_scanned())

if __name__ == '__main__':
    unittest.main()
