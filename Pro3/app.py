from dataclasses import field
from operator import contains
from flask import Flask, render_template, request, flash, redirect, url_for
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongopass import mongopass
import subprocess as sp
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField
from wtforms.validators import DataRequired,Length, Email,EqualTo, ValidationError
import os
import time

import pandas as pd
import json
import plotly
import plotly.express as px


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


import csv

SECRET_KEY = os.urandom(32)


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
data = {}
extracted_data = {}

@app.route('/',methods =['POST','GET'])
def jobHelp():
    date=sp.getoutput("date")
    # dat =  "April "
    # input("Press")
    if request.method == 'POST':
        username = request.form['username']
        fname = request.form['firstname']
        lname = request.form['lastname']
        address = request.form['address']
        city = request.form['city']
        pin = request.form['pin']
        state = request.form.get('state')
        email = request.form['email']
        phone = request.form['phone']
        phoneType = request.form['phoneType']
        url = request.form['url']

        #Work Experience
        job = request.form['exp']
        company = request.form['company']
        fromDate = request.form['from']
        toDate = request.form['to']
        location = request.form['location']
        desc = request.form['desc']

        #Education
        university = request.form['university']
        degree = request.form['degree']
        field = request.form['field']
        gpa = request.form['gpa']


        #Language
        language = request.form['languages']
        print(language)
        
        #Websites
        facebook = request.form['facebook']
        linkedin = request.form['linkedin']

        #Applications questions
        auth = request.form.get('auth')
        # auth = request.form['auth']
        sponsorship = request.form.get('sponsorship')
        relocation = request.form.get('relocation')
        loc = request.form['loc']
        agreement = request.form['agreement']
        salary = request.form['salary']
        travel = request.form['travel']

        gender = request.form.get('gender')
        print(gender)
        race = request.form['race']
        veteran = request.form.get('veteran')
        print(veteran)
        disability = request.form.get('disability')
        

        data['username']=username
        data['fname']=fname
        data['lname']=lname
        data['address']=address
        data['city']=city
        data['state']=state
        data['pin']=pin
        data['email']=email
        data['phone'] = phone
        data['phoneType'] = phoneType
        

        data['job']=job
        data['company']=company
        data['fromDate']=fromDate
        data['toDate']=toDate
        data['location']=location
        data['desc']=desc

        data['university']=university
        data['degree']=degree
        data['field']=field
        data['gpa']=gpa

        data['language']=language

        data['facebook']=facebook
        data['linkedin']=linkedin

        data['auth']=auth
        data['sponsorship']=sponsorship
        data['relocation']=relocation
        data['loc']=loc
        data['agreement']=agreement
        data['salary']=salary
        data['travel']=travel

        data['gender']=gender
        data['race']=race
        data['veteran']=veteran
        data['disability']=disability


        data['url']=url
        # data.append({'fname': fname,
        # 'lname': lname,
        # 'address':address,
        # 'city':city,
        # 'pin':pin,
        # 'email':email,
        # 'url': url})
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            existing_emails = [row[6] for row in reader]
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            existing_users = [row[0] for row in reader]

        if email in existing_emails:
            flash(f'****** Hello there!, Email {email} already exists ******  Enter only the JOB Url and username to proceed or Enter details for different email address')
            return redirect(url_for('jobHelp'))
        # if username in existing_users and email == "":
        #     print('username alert')
        #     flash(f'****** Hello there!, Username {username} already exists ******  SELECT A DIFFERENT USERNAME!')
        #     return redirect(url_for('jobHelp'))
        elif email != "":
            if username in existing_users:
                print('username alert')
                flash(f'****** Hello there!, Username {username} already exists ******  SELECT A DIFFERENT USERNAME!')
                return redirect(url_for('jobHelp'))
            else:
                with open('data.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow(data.values())
    print(data)
    return render_template("jobHelp.html", date=date)


@app.route('/fill_form', methods=['POST','GET'])
def fill_form():
    date=sp.getoutput("date")
    extracted_data['fname']=data['fname']
    extracted_data['lname']=data['lname']
    extracted_data['address']=data['address']
    extracted_data['city']=data['city']
    extracted_data['state']=data['state']
    extracted_data['pin']=data['pin']
    extracted_data['email']=data['email']
    extracted_data['phone']=data['phone']
    extracted_data['phoneType']=data['phoneType']
    #Enter job details
    extracted_data['job']=data['job']
    extracted_data['company']=data['company']
    extracted_data['fromDate']=data['fromDate']
    extracted_data['toDate']=data['toDate']
    extracted_data['location']=data['location']
    extracted_data['desc']=data['desc']
    #Enter education Details
    extracted_data['university']=data['university']
    extracted_data['degree']=data['degree']
    extracted_data['field']=data['field']
    extracted_data['gpa']=data['gpa']
    #language
    extracted_data['language']=data['language']
    #Websites
    extracted_data['facebook']=data['facebook']
    extracted_data['linkedin']=data['linkedin']
    #Applications questions
    extracted_data['auth']=data['auth']
    extracted_data['sponsorship']=data['sponsorship']
    extracted_data['relocation']=data['relocation']
    extracted_data['loc']=data['loc']
    extracted_data['agreement']=data['agreement']
    extracted_data['salary']=data['salary']
    extracted_data['travel']=data['travel']

    extracted_data['gender']=data['gender']
    extracted_data['race']=data['race']
    extracted_data['veteran']=data['veteran']
    extracted_data['disability']=data['disability']

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)

        # Read the header row
        header = next(reader)

        # Find the index of the 'Name' column
        username_index = header.index('username')
        email_index = header.index('email')

        for row in reader:
            if row[username_index] == data['username'] or row[email_index] == data['username']:
                extracted_data['fname']=row[header.index('First Name')]
                extracted_data['lname']=row[header.index('Last Name')]
                extracted_data['address']=row[header.index('Address')]
                extracted_data['city']=row[header.index('City')]
                extracted_data['state']=row[header.index('State')]
                extracted_data['pin']=row[header.index('pincode')]
                extracted_data['email']=row[header.index('email')]
                extracted_data['phone']=row[header.index('Phone Number')]
                extracted_data['phoneType']=row[header.index('Phone Device Type')]

                #Enter job details
                extracted_data['job'] =  row[header.index('Job Title')]
                extracted_data['company'] = row[header.index('Company')]
                extracted_data['fromDate']= row[header.index('From')]
                extracted_data['toDate']= row[header.index('To')]
                extracted_data['location']= row[header.index('Location')]
                extracted_data['desc']= row[header.index('Description')]

                #Enter Education details
                extracted_data['university'] =  row[header.index('University')]
                extracted_data['degree'] = row[header.index('Degree')]
                extracted_data['field']= row[header.index('Field')]
                extracted_data['gpa']= row[header.index('GPA')]
                extracted_data['language']= row[header.index('language')]
                extracted_data['facebook']= row[header.index('Facebook')]
                extracted_data['linkedin']= row[header.index('LinkedIn')]

                #Application questions
                extracted_data['auth']= row[header.index('Authorized to Work?')]
                extracted_data['sponsorship']=row[header.index('Require sponsorship?')]
                extracted_data['relocation']=row[header.index('Open to relocation?')]
                extracted_data['loc']=row[header.index('Current location')]
                extracted_data['agreement']=row[header.index('non-compete or non- solicitation agreement?')]
                extracted_data['salary']=row[header.index('Salary expectations')]
                extracted_data['travel']=row[header.index('Willing to travel?')]

                extracted_data['gender']=row[header.index('Gender')]
                extracted_data['race']=row[header.index('race')]
                extracted_data['veteran']=row[header.index('Are you veteran?')]

                extracted_data['disability']=row[header.index('Do you have Disability?')]


                print(f"First Name: {row[header.index('First Name')]}")
                break

    # Set up web driver
    service = Service('/path/to/chromedriver')
    driver = webdriver.Chrome(service=service)
    # driver.implicitly_wait(10)
    driver.get(data['url'])
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    label_element = driver.find_element(By.XPATH, "//label[contains(text(), 'First Name')]")
    for_attr = label_element.get_attribute("for")
    input_field = driver.find_element(By.XPATH, f"//*[@id='{for_attr}']")

    input_field.send_keys(extracted_data['fname'])
    driver.implicitly_wait(10)

    input_field = driver.find_element(By.XPATH, "//input[contains(@name, 'last')]")
    input_field.send_keys(extracted_data['lname'])

    input_field = driver.find_element(By.XPATH, "//input[contains(@name, 'address')]")
    input_field.send_keys(extracted_data['address'])

    input_field = driver.find_element(By.XPATH, "//input[contains(@name, 'city')]")
    input_field.send_keys(extracted_data['city'])

    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'region')]")
    select = Select(input_field)
    str1= extracted_data['state']
    select.select_by_visible_text(str1)

    input_field = driver.find_element(By.XPATH, "//input[contains(@name, 'postal')]")
    input_field.send_keys(extracted_data['pin'])

    input_field = driver.find_element(By.XPATH, "//input[contains(@name, 'email')]")
    input_field.send_keys(extracted_data['email'])

    input_field = driver.find_element(By.XPATH, "//input[contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'phone') and contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'number')]")
    input_field.send_keys(extracted_data['phone'])

    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'deviceType')]")
    select = Select(input_field)
    str1= extracted_data['phoneType']
    select.select_by_visible_text(str1)

    
    # time.sleep(10)
    # print('waiting for 30seconds')

    inputs = driver.find_elements(By.XPATH,'//input[@required]')
    inputs.extend(driver.find_elements(By.XPATH,'//select[@required]'))
    # inputs= driver.find_elements(By.XPATH, "//label[contains(text(), '*')]/following-sibling::input")
    for field in inputs:
        driver.execute_script("arguments[0].setAttribute('required', 'true');", field)
    

    next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
    while True:
        # Check if all the required fields have been filled out

        all_fields_filled = True
        for field in inputs:
            if field.get_attribute("value") == "":
                all_fields_filled = False
                break
            else:
                all_fields_filled=True
            # If all required fields are filled, click on the Next button and break out of the loop
        if all_fields_filled:
            print('next button pressed')
            next_button.click()
            break

        # If any of the required fields are empty, wait for a few seconds and check again
        time.sleep(10)
        # next_button.click()

    time.sleep(5)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'title')]")))


    input_field = driver.find_element(By.XPATH, "//input[contains(@id, 'title')]")
    actions = ActionChains(driver)
    actions.move_to_element(input_field)
    actions.click()
    actions.send_keys(' ')
    actions.perform()

    input_field.send_keys(extracted_data['job'])

    input_field = driver.find_element(By.XPATH, "//input[contains(@id, 'company')]")
    input_field.send_keys(extracted_data['company'])

    input_field = driver.find_element(By.XPATH, "//input[contains(@id, 'startDate')]")

    actions = ActionChains(driver)
    actions.move_to_element(input_field)
    actions.click()
    actions.send_keys(extracted_data['fromDate'])
    actions.perform()
    # input_field.send_keys(extracted_data['fromDate'])

    input_field = driver.find_element(By.XPATH, "//input[contains(@id, 'endDate')]")
    actions = ActionChains(driver)
    actions.move_to_element(input_field)
    actions.click()
    actions.send_keys(extracted_data['toDate'])
    actions.perform()

    input_field = driver.find_element(By.XPATH, "//input[contains(@id, 'location')]")
    input_field.send_keys(extracted_data['location'])

    input_field = driver.find_element(By.XPATH, "//textarea[contains(@id, 'Description')]")
    input_field.send_keys(extracted_data['desc'])
    # input_field.send_keys(extracted_data['toDate'])

    # next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
    # next_button.click()

    input_field = driver.find_element(By.XPATH, "//input[contains(@id, 'school')]")
    input_field.send_keys(extracted_data['university'])

    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'degree')]")
    select = Select(input_field)
    select.select_by_visible_text(extracted_data['degree'])
    input_field.send_keys(extracted_data['degree'])

    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'field')]")
    select = Select(input_field)
    str1= extracted_data['field'].title()
    select.select_by_visible_text(str1)
    input_field.send_keys(extracted_data['field'])

    input_field = driver.find_element(By.XPATH, "//input[contains(@label, 'GPA')]")
    input_field.send_keys(extracted_data['gpa'])

    # if(driver.find_element(By.XPATH, "//button[contains(@id, 'language')]")):
    #     lang_button = driver.find_element(By.XPATH, "//button[contains(@id, 'language')]")
    #     lang_button.click()
    #     input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'language')]")
    #     select = Select(input_field)
    #     str1= extracted_data['language'].title()
    #     print(str1)
    #     select.select_by_visible_text(str1)

    # if(driver.find_element(By.XPATH, "//button[contains(@id, 'language')]")):
    #     lang_button = driver.find_element(By.XPATH, "//button[contains(@id, 'language')]")
    #     lang_button.click()

    
    input_field = driver.find_element(By.XPATH, "//input[contains(@label, 'Facebook')]")
    input_field.send_keys(extracted_data['facebook'])

    input_field = driver.find_element(By.XPATH, "//input[contains(@label, 'Linkedin')]")
    input_field.send_keys(extracted_data['linkedin'])


    inputs = driver.find_elements(By.XPATH,'//input[@required]')
    inputs.extend(driver.find_elements(By.XPATH,'//select[@required]'))
    # inputs= driver.find_elements(By.XPATH, "//label[contains(text(), '*')]/following-sibling::input")
    for field in inputs:
        driver.execute_script("arguments[0].setAttribute('required', 'true');", field)

    next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
    while True:
        # Check if all the required fields have been filled out

        all_fields_filled = True
        for field in inputs:
            if field.get_attribute("value") == "":
                all_fields_filled = False
                break
            else:
                # print(field.get_attribute("value"))
                all_fields_filled=True
            # If all required fields are filled, click on the Next button and break out of the loop
        if all_fields_filled:
            print('next button pressed')
            next_button.click()
            break

        # If any of the required fields are empty, wait for a few seconds and check again
        time.sleep(10)
        # next_button.click()

    time.sleep(5)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'authorized')]")))

    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'Primary 1')]")
    select = Select(input_field)
    str1= extracted_data['auth'].title()
    select.select_by_visible_text(str1)

    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'Primary 4')]")
    select = Select(input_field)
    str1= extracted_data['sponsorship'].title()
    select.select_by_visible_text(str1)

    inputs = driver.find_elements(By.XPATH,'//input[@required]')
    inputs.extend(driver.find_elements(By.XPATH,'//select[@required]'))
    for field in inputs:
        driver.execute_script("arguments[0].setAttribute('required', 'true');", field)
    next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
    while True:
        all_fields_filled = True
        for field in inputs:
            if field.get_attribute("value") == "":
                all_fields_filled = False
                break
            # else:
            #     print(field.get_attribute("value"))
                all_fields_filled=True
        if all_fields_filled:
            print('next button pressed')
            next_button.click()
            break
        time.sleep(10)
        # next_button.click()

    time.sleep(5)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'relocation')]")))
    
    input_field = driver.find_element(By.XPATH, "//textarea[contains(@id, 'secondaryJsqData.NA Secondary Internal/External General.QUESTION_SETUP-3-189')]")
    input_field.send_keys(extracted_data['relocation'])

    input_field = driver.find_element(By.XPATH, "//textarea[contains(@id, 'Candidate location')]")
    input_field.send_keys(extracted_data['loc'])
    
    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'Non compete agreement')]")
    select = Select(input_field)
    str1= extracted_data['agreement'].title()
    select.select_by_visible_text(str1)

    input_field = driver.find_element(By.XPATH, "//textarea[contains(@id, 'Salary')]")
    input_field.send_keys(extracted_data['salary'])

    input_field = driver.find_element(By.XPATH, "//textarea[contains(@id, 'Travel')]")
    input_field.send_keys(extracted_data['travel'])

    inputs = driver.find_elements(By.XPATH,'//input[@required]')
    inputs.extend(driver.find_elements(By.XPATH,'//select[@required]'))
    for field in inputs:
        driver.execute_script("arguments[0].setAttribute('required', 'true');", field)
    next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
    while True:
        all_fields_filled = True
        for field in inputs:
            if field.get_attribute("value") == "":
                all_fields_filled = False
                break
            else:
                all_fields_filled=True
        if all_fields_filled:
            print('next button pressed')
            next_button.click()
            break
        time.sleep(10)
        # next_button.click()

    time.sleep(5)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'gender')]")))
    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'gender')]")
    select = Select(input_field)
    str1= extracted_data['gender'].title()
    select.select_by_visible_text(str1)

    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'ethnicity')]")
    select = Select(input_field)
    options = select.options
    for option in options:
        if extracted_data['race'].lower() in option.text.lower():
            option.click()
            break

    input_field = driver.find_element(By.XPATH, "//select[contains(@id, 'veteran')]")
    select = Select(input_field)
    str1= extracted_data['veteran']
    select.select_by_visible_text(str1)

    inputs = driver.find_elements(By.XPATH,'//input[@required]')
    inputs.extend(driver.find_elements(By.XPATH,'//select[@required]'))
    for field in inputs:
        driver.execute_script("arguments[0].setAttribute('required', 'true');", field)
    next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
    while True:
        all_fields_filled = True
        for field in inputs:
            if field.get_attribute("value") == "":
                all_fields_filled = False
                break
            else:
                all_fields_filled=True
        if all_fields_filled:
            print('next button pressed')
            next_button.click()
            break
        time.sleep(10)

    time.sleep(5)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@id, 'disability')]")))
    if 'NO' in extracted_data['disability']:
        radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and contains(@name, 'disability') and contains(@value, \"NO\")]")
    elif 'YES' in extracted_data['disability']:
        radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and contains(@name, 'disability') and contains(@value, \"YES\")]")
        # radio_button = driver.find_element(By.XPATH,"//input[@type='radio' and contains(@name, 'disability') and contains(@value, 'YES'")
    else:
        radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and contains(@name, 'disability') and contains(@value, \"DECLINE\")]")
    radio_button.click()
    next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
    next_button.click()

    





    # radio_button = driver.find_element(By.XPATH,"//input[@type='radio' and contains(@name, 'disability')]//following-sibling::span(contains(text() extracted_data['disability'])")
    # radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and contains(@name, 'disability') and contains(span/text(), '" + extracted_data['disability'] + "')]")


    # print(extracted_data['disability'])
    # print(radio_button)
    # radio_button.click()

#https://careers.alight.com/us/en/apply?jobSeqNo=ALIGUSR21285EXTERNALENUS&step=1
    input("something")
    return render_template("fill_form.html", date=date)
if __name__ == '__main__':
    app.run(debug=True)
