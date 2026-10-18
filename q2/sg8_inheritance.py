class publication:
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
    print("Title:", get_title())
    print("Author:", get_author())

class book:
  def __init__(self, title, author, number_of_pages):
    super().__init__(self, title, author):
    self.__number_of_pages = number_of_pages
  def set_number_of_pages(self, number_of_pages):
    self.number_of_pages = number_of_pages
  def get_number_of_pages(self):
    return self.number_of_pages

class magazine:
  def __init__(self, title, author, issue_number):
    super().__init__(self, title, author):
    self.issue_number = issue_number
    def set_issue_number(self, issue_number):
    self.issue_number = issue_number
   def get_issue_number(self):
     return self.issue_number

pub1 = publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = magazine("National Geographic", "Various Authors", 202)

print("Publication Information")
pub1.display_info()


