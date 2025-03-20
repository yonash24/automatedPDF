"""Categorizes documents based on keywords"""

class DocumentCategorizer:
    categories = {
        "invoice": {"invoice", "bill", "amount due"},
        "report": {"report", "summary", "analysis"},
        "contract": {"agreement", "contract", "terms"},
    }
    
    def categorize_document(self, text: str):
        """Determines the category of a document based on keywords"""
        if not text:
            return "uncategorized"
        
        words = set(text.lower().split())
        for category, keyword in self.categories.items():
            if words & keyword:
                return category
        return "uncategoraized"
        
        
    
    def add_category(self, category_name: str, keyword_list: set):
        """Adds a new document category"""
        if category_name in self.categories:
            return f"category: {category_name} already exist"
        
        self.categories[category_name] = set(keyword_list)
        return f"category: {category_name} added successfully"
    
    def remove_category(self, category_name: str):
        """Removes a document category"""
        if category_name not in self.categories:
            return f"category {category_name} does not exist"
        
        del self.categories[category_name]
        return f"category {category_name} removed successfully"