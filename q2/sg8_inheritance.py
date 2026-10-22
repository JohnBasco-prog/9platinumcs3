class Publication:
  def __init__(self,title,author):
    self.__title = title
    self.__author = author

  def set_title(self,title):
     self.__title = title
 
  def get_title(self):
    return self.__title
  
  def set_author(self,author):
    self.__author = author
  
  def get_author(self):
    return self.__author
  
  def display_info(self):
    print("Title:", self.get_title())
    print("Author:", self.get_author())

class Book(Publication):
  def __init__(self, title, author, number_of_pages):
    super().__init__(title, author)
    self.set_number_of_pages(number_of_pages)
    self.__number_of_pages = 0
    
  
  def set_number_of_pages(self, number_of_pages):
      if self.__number_of_pages > 0:
      self.__number_of_pages = number_of_pages

      else: 
        print("Number of pages must be positive")
  
  def display_info(self):
    super().display_info()
    print("Number of pages:", self.get_number_of_pages())

class Magazine(Publication):
  def __init__(self, title, author, issue_number)
    super().__init__(title, author):
    self.__issue_number = 0
    self.set_issue_number(issue_number)
  
  def set_issue_number(self, issue_number):
       if self.__number_of_pages > 0:
      self.__number_of_pages = number_of_pages

      else: 
        print("Number of pages must be positive")
   
  def get_issue_number(self):
     return self.issue_number
  def display_info(self):
    super().display_info()
    print("Issue number:", self.get_issue_number())

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information")
pub1.display_info()
print("Book Information")
book1.display_info()
print("Magazine Information")
mag1.display_info()
