from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import json


def main():
	print "\n\t\tLETS   SCRAP !!\n\n"
	"""
			Start a web driver using selenium
	"""
	driver = webdriver.Firefox()

	"""
			Stage 1
	---------------------------------------------------------------------------
			Open the base URL in web browser -Firefox

	"""
	
	driver.get('http://www.mciindia.org/InformationDesk/IndianMedicalRegister.aspx')

	"""
			Stage 2
	---------------------------------------------------------------------------
			Search About College Assessment For Year 2014
	"""
	
	state_medical_council = driver.find_element_by_xpath(".//*[@id='dnn_ctr588_IMRIndex_Link_Council']")
	state_medical_council.click()
	
	# Page changes Dynamically
	# Search For State - Delhi
	
	state_name = driver.find_element_by_xpath(".//*[@id='dnn_ctr588_IMRIndex_Drp_StateCouncil']/option[9]")
	state_name.click()
	
	"""
			Click Submit

	"""

	submit = driver.find_element_by_xpath(".//*[@id='dnn_ctr588_IMRIndex_Submit_Btn']")
	submit.click()

	"""
			Stage 3
	---------------------------------------------------------------------------

	Clicking The View button for particular Person And Open the Pop Up Window

	"""
	print "\n\t\t LETS VIEW THE DETAILS\n\n"

	data = []
	for loop in range(0,330):
		for i in range(3,33):
			doctors = {}
			
			check = 0
			while not check:
				try:
					if i<10:
						click_view = driver.find_element_by_xpath(".//*[@id='dnn_ctr588_IMRIndex_GV_Search_ctl0"+str(i)+"_lbl']")
						check = 1
					elif i>9:
						click_view = driver.find_element_by_xpath(".//*[@id='dnn_ctr588_IMRIndex_GV_Search_ctl"+str(i)+"_lbl']")
						check = 1
				except NoSuchElementException:
					time.sleep(2)
			
			#parent handle
			parent_window = driver.current_window_handle
			
			#switch to details window
			click_view.click()
			
			time.sleep(0.5)

			handles = driver.window_handles
			handles.remove(parent_window)
			driver.switch_to_window(handles.pop())

			s_no = ( loop *30 ) + i - 2
			name = driver.find_element_by_xpath(".//*[@id='Name']").text
			fname = driver.find_element_by_xpath(".//*[@id='FatherName']").text
			dob = driver.find_element_by_xpath(".//*[@id='DOB']").text
			yearofinfo = driver.find_element_by_xpath(".//*[@id='lbl_Info']").text
			regno = driver.find_element_by_xpath(".//*[@id='Regis_no']").text
			dateofreg = driver.find_element_by_xpath(".//*[@id='Date_Reg']").text
			smc = driver.find_element_by_xpath(".//*[@id='Lbl_Council']").text
			qualification = driver.find_element_by_xpath(".//*[@id='Qual']").text
			qualyear = driver.find_element_by_xpath(".//*[@id='QualYear']").text
			univ = driver.find_element_by_xpath(".//*[@id='Univ']").text
			address = driver.find_element_by_xpath(".//*[@id='Address']").text

			#save data in doctors
			doctors["s_no"] = s_no
			doctors["name"] = name
			doctors["fname"] = fname
			doctors["dob"] = dob
			doctors["yearofinfo"] = yearofinfo
			doctors["regno"] = regno
			doctors["dateofreg"] = dateofreg
			doctors["qualification"] = qualification
			doctors["qualyear"] = qualyear
			doctors["univ"] = univ
			doctors["address"] = address

			#Append the Data
			data.append(doctors)

			driver.switch_to_window(parent_window)
		#if loop =0 then next tag is at [1]

		#else next tag is at [3] 

		if loop == 0:	
			check = 0
			while not check:
				try:
					next_page = driver.find_element_by_xpath(".//*[@id='dnn_ctr588_IMRIndex_GV_Search']/tbody/tr[33]/td/table/tbody/tr/td[1]/a")
					check = 1

				except NoSuchElementException:
					time.sleep(2)

			next_page.click()

			time.sleep(2)
		else :
			check = 0
			while not check:
				try:
					next_page = driver.find_element_by_xpath(".//*[@id='dnn_ctr588_IMRIndex_GV_Search']/tbody/tr[33]/td/table/tbody/tr/td[3]/a")
					check = 1

				except NoSuchElementException:
					time.sleep(2)

			next_page.click()

	"""
			Stage 4
	---------------------------------------------------
			Dumps the data

	"""

	myfile = open("data.json","w")
	myfile.write(json.dumps(data))

	driver.close()

	# Completed

	print "\n\t\tSCRAPING IS DONE!! Thank God !!\n\n"
if __name__ == '__main__':
	main()
