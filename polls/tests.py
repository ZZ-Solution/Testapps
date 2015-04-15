from django.test import TestCase
from polls.models import Question, Choice
from django.utils import timezone

class QuestionTests(TestCase):
	def test_str(self):
		contact = Question(question_text="sandeep")
		self.assertEquals(str(contact),"sandeep")

class ChoiceTests(TestCase):
	def test_choice(self):
		choice = Choice(question = "sandeep", choice_text = "choice text testing")
		self.assertEquals(str(choice), "sandeep", "choice text testing")