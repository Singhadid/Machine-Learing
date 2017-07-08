import numpy as np
import characterizer as c
import pandas as pd
import types

class charact_applier():
	def __init__(self):
		pathfile = "/Users/nnn./Desktop/train.csv"
		df = (pd.read_csv(pathfile)).astype(str)
		self.c1 = df["# Customer_ID"]
		self.c2 = df["Sessions"]
		self.c3 = df["Cell_ID"]
		self.c4 = df["District_ID"]
		self.c5 = df["Complaints_U"]
		self.c6 = df["Complaints_R"]
		self.c7 = df["Complaints_W"]
		self.c8 = df["Label"]
		self.r_dir = dir(c.function_all)
		self.func = []
	def filter_func(self):
		for x in range(0,len(self.r_dir)):
			if "_" != self.r_dir[x][0] and "_" != self.r_dir[x][1]:
				self.func.append(self.r_dir[x])
		return charact_applier().check_type(self.func)
	"""def check_type(self):"""

if __name__ == '__main__':
	var = c.function_all()
	char = charact_applier()
	"""df = pd.DataFrame({'f1-character_only': var.character_only(char.c1), 'f2-digit_only': var.digit_only(char.c1)
		              ,'f3-capitalletters_only': var.capitalletters_only(char.c1), 'f4-smallletters_only': var.smallletters_only(char.c1)
		              ,'f5-specialcharacter_only': var.specialcharacter_only(char.c1), 'f6-specialcharacter': var.specialcharacter(char.c1)
		              ,'f7-count_length':var.count_length(char.c1), 'f8-count_number': var.count_number(char.c1), 'f9-count_capitalletters':var.count_capitalletters(char.c1)
		              ,'f10-count_smallletters':var.count_smallletters(char.c1), 'f11-count_specialcharacter': var.count_specialcharacter(char.c1),'f12':var.count_dot(char.c1)
		              ,'f13-count_forwardslash':var.count_forwardslash(char.c1), 'f14-count_dash': var.count_dash(char.c1), 'f15-count_comma': var.count_comma(char.c1)
		              ,'f16-date': var.date(char.c1),'f17-digit_comma': var.digit_comma(char.c1)})
	print(df)"""


	

