#!/usr/bin/env python3

class MyString:

  def __init__(self, value=None) :
    self._value = None
    if value is not None:
            self.value = value

  @property
  def value(self):
        return self._value
  
  @value.setter
  def value (self, new_value):
     if isinstance (new_value, str):
        self._value = new_value

     else :
        print ("The value must be a string.")

  def is_sentence(self):
     if self._value is not None:
        return self._value.endswith (".")
     return False

  def is_question(self):
      if self._value is not None:
        return self._value.endswith ("?")
      return False

  def is_exclamation(self):
      if self._value is not None:
        return self._value.endswith ("!")
      return False
  
  def count_sentences(self):
     if self._value is None:
            return 0
     
     separators = ['.', '!', '?']
     for separator in separators:
            self._value = self._value.replace(separator, '.')

     sentences = self._value.split('.')
     sentences = [sentence for sentence in sentences if sentence.strip() != '']
     return len(sentences)
    

  
     
