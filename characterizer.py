import numpy as np
import string
import math
class function_all():
	def __init__(self):
		self.data_digit = []
		self.data_character = []
		self.data_date = []
		self.data_date1 = []
		self.data_specialchar_only = []
		self.data_specialchar = []
		self.data_capitalletter = []
		self.data_smallletter = []
		self.data_countnumber = []
		self.data_countcapitalletter = []
		self.data_countsmallletter = []
		self.data_countspecialchar = []
		self.data_countlength = []
		self.data_countdot = []
		self.data_countforwardslash = []
		self.data_countdash = []
		self.data_countcomma = []
		self.data_digitplus = []
		self.avg = 0
		self.max = 0
		self.min = 0
		self.sd = 0
	def character_only(self,data):
		for x in range(0,len(data)):
			try:
				if data[x].isalpha():
					self.data_character.append(True)
				else:
					self.data_character.append(False)
			except Exception:
				self.data_character.append(False)
		return self.data_character
	def digit_only(self,data):
		for x in range(0,len(data)):
			try:
				if data[x].replace('.','').isdigit():
					self.data_digit.append(True)
				else:
					self.data_digit.append(False)
			except Exception:
				self.data_digit.append(False)
		return self.data_digit
	def capitalletters_only(self,data):
		for x in range(0,len(data)):
			try:
				if data[x].isupper():
					self.data_capitalletter.append(True)
				else:
					self.data_capitalletter.append(False)
			except Exception:
				self.data_capitalletter.append(False)
		return self.data_capitalletter
	def smallletters_only(self,data):
		for x in range(0,len(data)):
			try:
				if data[x].islower():
					self.data_smallletter.append(True)
				else:
					self.data_smallletter.append(False)
			except Exception:
				self.data_smallletter.append(False)
		return self.data_smallletter
	def specialcharacter_only(self,data):
		"""~`!@#$%^&*()_-+={}[]:>;',</?*-+"""
		for x in range(0,len(data)):
			count = 0
			invalidChars = set(string.punctuation.replace("_", ""))  
			for i in data[x]:
			 	if i in invalidChars:
			 		count +=1
			 		if count == len(data[x]):
			 			self.data_specialchar_only.append(True)
			 	else:
			 		self.data_specialchar_only.append(False)
			 		break
		return self.data_specialchar_only
	def specialcharacter(self,data):
		"""~`!@#$%^&*()_-+={}[]:>;',</?*-+"""
		invalidChars = set(string.punctuation.replace("_", ""))
		for x in range(0,len(data)):
			if any(char in invalidChars for char in data[x]):
	  	 	 	self.data_specialchar.append("Specialchar")
			else:
	  	  		self.data_specialchar.append("No-Specialcar")
		return self.data_specialchar 
	def count_length(self,data):
		for x in range(0,len(data)):
			self.data_countlength.append(len(data[x]))
		return 	self.data_countlength
	def count_number(self,data):
		number = "0123456789"
		for x in range(0,len(data)):
			count = 0 
			for i in data[x]:
				if i in number:
					count += 1
			self.data_countnumber.append(count)
		return self.data_countnumber
	def count_capitalletters(self,data):
		for x in range(0,len(data)):
			count = 0 
			for i in data[x]:
				if i.isupper():
					count +=1
			self.data_countcapitalletter.append(count)
		return self.data_countcapitalletter
	def count_smallletters(self,data):
		for x in range(0,len(data)):
			count = 0 
			for i in data[x]:
				if i.islower():
					count +=1
			self.data_countsmallletter.append(count)
		return self.data_countsmallletter
	def count_specialcharacter(self,data):
		"""~`!@#$%^&*()_-+={}[]:>;',</?*-+"""
		invalidChars = set(string.punctuation.replace("_", ""))
		for x in range(0,len(data)):
			count = 0 
			for i in data[x]:
				if i in invalidChars:
					count +=1
			self.data_countspecialchar.append(count)
		return self.data_countspecialchar
	def count_dot(self,data):
		symbol = "."
		for x in range(0,len(data)):
			count = 0
			for i in data[x]:
				if i in symbol:
					count += 1
			self.data_countdot.append(count)
		return self.data_countdot
	def count_forwardslash(self,data):
		symbol = "/"
		for x in range(0,len(data)):
			count = 0
			for i in data[x]:
				if i in symbol:
					count += 1
			self.data_countforwardslash.append(count)
		return self.data_countforwardslash
	def count_dash(self,data):
		symbol = "-"
		for x in range(0,len(data)):
			count = 0
			for i in data[x]:
				if i in symbol:
					count += 1
			self.data_countdash.append(count)
		return self.data_countdash
	def count_comma(self,data):
		symbol = ","
		for x in range(0,len(data)):
			count = 0
			for i in data[x]:
				if i in symbol:
					count += 1
			self.data_countcomma.append(count)
		return self.data_countcomma
	def date(self,data):
		symbol = "/"
		for x in range(0,len(data)):
			count = 0 
			length = 0
			for i in data[x]:
				if i in symbol:
					count += 1
					length +=1
				else:
				    length +=1 
				if len(data[x]) == length:
					self.data_date.append(count)
		for y in range(0,len(self.data_date)):
			if self.data_date[y] == 2:
				if data[y][-4:].isdigit():
					self.data_date1.append("date")
			else:
				self.data_date1.append("no-date")

		return self.data_date1 
	def digit_comma(self,data):
		symbol = ","
		for x in range(0,len(data)):
			count = 0
			for i in data[x]:
				if i in symbol:
					count +=1
					if (data[x].replace(symbol,'')).isdigit():
						self.data_digitplus.append("digit-comma")
					else:
						self.data_digitplus.append("Non-digit-comma")
						break
				else:
					count +=1
					if count == len(data[x]):
						self.data_digitplus.append("Non-digit-comma")
		return self.data_digitplus
	def average(self,data):
		self.avg = np.mean(data)
		return self.avg
	def maximum(self,data):
		self.max = np.max(data)
		return self.max
	def minimum(self,data):
		self.min = np.min(data)
		return self.min
	def std_dev(self,data):
		self.sd = np.std(data)
		return self.sd
	def all_true(data):

		return all(data) is True
	def all_false(data):
		return all(data) is False
	def any_true(data):

		return any(data) is True
	def any_false(data):

		return any(data) is False
	def true_proportion(data):
		count_true = 0
		count_false = 0
		for x in range(0,len(data)):
			if data[x] is True:
				count_true += 1
			elif data[x] is False:
				count_false += 1
		return count_true/count_false
	def false_proportion(data):
		count_true = 0
		count_false = 0
		for x in range(0,len(data)):
			if data[x] is True:
				count_true += 1
			elif data[x] is False:
				count_false += 1
		return count_false/count_true
		








