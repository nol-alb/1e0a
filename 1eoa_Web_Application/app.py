import sys, os
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField
import csv
import functions as pro
import librosa
import pandas as pd
import warnings
from flask_sslify import SSLify


outPath = ''
fs = 44100
l4 = ['1111','1010','1001','1101','0001','0110','111','110','001','010','11111','10100','10110','11101','11011','10101','01010','1111111','1111000','1101100','0100101','0001010','0111010'] 


app = Flask(__name__,
            static_folder='static',
            template_folder='templates')


app.secret_key = os.urandom(24)
app.debug = True

def nextcycle(cycle):
	path = 'static/Data/csv_complexity/compdict'+str(cycle)+'.csv'
	filename = path
	df=pd.read_csv(filename,dtype={'Pattern':object})
	return df

def next_pattern(cyclelength,s1):
	next_cycle_length = {4:3,3:5,5:7}
	init_cycle_pattern = {4:'1111',3:'111',5:'11111',7:'1111111'}

	s=format(str(s1),'>0'+str(cyclelength))
	df=pd.read_csv('static/Data/csv_complexity/compdict'+str(cyclelength)+'.csv',dtype={'Pattern':object})
	df['Pattern']=df['Pattern'].astype(str)
	df['Complexity']=df['Complexity'].astype(float)
   
	current_complexity=df[df['Pattern']==s]['Complexity'].iloc[0]
	subdf=df[(df['Complexity']>=current_complexity)&(df['Pattern']!=s)].sort_values(by='Complexity')
	if subdf.shape[0]>0:
		temp=subdf['Pattern'].head(1)
		patt=temp.values[0]
		next_pattern=format(str(patt), '>0'+str(cyclelength))
	else:
		cyclelength=next_cycle_length[cyclelength]
		patt = init_cycle_pattern[cyclelength]
		next_pattern=format(str(patt), '>0'+str(cyclelength))
	return next_pattern,cyclelength

def nextpattern(df,s,cycle):
	sub = df[(df['Pattern']==s)].index[0]  
	sub = sub+1
	val = df["Pattern"].iloc[sub]
	val = str(val).zfill(cycle)
	return val
def str_int_list(z):
	j = list(str(z)) 
	cnt = 0 
	for i in j: 
		j[cnt]=int(i) 
		cnt=cnt+1
	return j
def create_csv(name):
	path = 'static/Data/Users/'+name+'/results/results.csv'
	with open(path, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["Pattern","Cycle Length","Name"])
	file.close()

	return 0

def uppend_csv(pattern, cycle, name):
	path = 'static/Data/Users/'+name+'/results/results.csv'
	with open(path, mode='a', newline='') as file:
		data = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		data.writerow([pattern,cycle,name])


		filename = './static/Data/Register.csv'
		df=pd.read_csv(filename,dtype={'Pattern':object})
		df.loc[(df['Name']==name),'CycleLength']=cycle
		df.loc[(df['Name']==name),'Pattern']=pattern
		df.to_csv(filename,index=False)
	
		outname1='./static/Data/Users/'+name+'/results/temp'
		import os
		os.remove(outname1)

	file.close()
	return 0








def patterngen(bpm,cycle,s=[]):
	x,onsetgen, fs = pro.metronome(bpm,cycle,s)
	return x,onsetgen,fs
def newdir(name):
	direc = 'static/Data/Users/' + name
	direcrec = direc + '/recordings'
	direcgen = direc + '/GenSounds'
	direcimages = direc + '/results'
	os.makedirs(direc)
	os.makedirs(direcgen)
	os.makedirs(direcrec)
	os.makedirs(direcimages)
	return 0


def confirm_login_pw(loginid,pw):
	filename='static/Data/Register.csv'
	df=pd.read_csv(filename,dtype={'Pattern':object})
	sub=df[(df['Name']==loginid)&(df['Password']==pw)]
	if sub.shape[0]>0:
		return True
	else:
		return False
def get_current_state(loginid):
	filename='static/Data/Register.csv'
	df=pd.read_csv(filename,dtype={'Pattern':object})
	sub=df[(df['Name']==loginid)]
	return sub['Pattern'].values,sub['CycleLength'].values

@app.route("/", methods=['POST', 'GET'])
def index():
	if request.method == "POST":
		name = session['username']
		pattern = session['pattern']
		f = request.files['audio_data']
		outname='./static/Data/Users/'+name+'/recordings/audio'+pattern+'.wav'
		with open(outname, 'wb') as audio:
			f.save(audio)
			outname1='./static/Data/Users/'+name+'/results/temp'
			from pathlib import Path
			Path(outname1).touch()

			
	else:
		return render_template('home.html')


# home function
@app.route('/profile/<int:id>')
def myProfile(id):
    return 'The project page'
# projects function
@app.route('/projects/')
def projects():
    return url_for('myProfile', id=1)
@app.route('/home')
def temp():
	return render_template('home.html')


@app.route('/startlearning', methods=['POST', 'GET'])
def learn():
		pattern = session['pattern']
		cntr = l4.index(pattern)
		cntr = cntr+1
		cycle = session['cycle']
		name = session['username']
		pattern = str_int_list(pattern)
		x,onsetgen, fs = patterngen(160,cycle,pattern)
		pattern = session['pattern']
		path = pro.audiowrite(x, fs, name,pattern)
		path = '../'+path
		outPath = os.path.join(path)
		if request.method == "POST":
			audiocheck = './static/Data/Users/'+name+'/recordings/audio'+str(pattern)+'.wav'
			isExist = os.path.exists(audiocheck)
			if (isExist == False):
				return render_template('StartLearning.html', songout = outPath, name = name, pattern=pattern,isExist=isExist)


			pattern = str_int_list(pattern)
			averagebeat, averagecycle,n = pro.errordet(audiocheck,fs,onsetgen,pattern)
		
			pattern = session['pattern']
			j = pro.plotter(averagebeat,averagecycle,name,[str(pattern)])
			j = '../'+j
			session['plotpath'] = j
			return redirect(url_for('dashboard', n=n))
		return render_template('StartLearning.html', songout = outPath, name = name, pattern=pattern,cntr=cntr)


 

@app.route('/CheckUser')
def Checkuser():
  with open('static/Data/Register.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    users = []
    for row in data:
      if not first_line:
        users.append({
          "Name": row[0],
          "Musician": row[1],
          "IfyeswhichInstrument": row[2],
          "yrsofexp": row[3],
          "Pattern": row[5],
          "Cycle": row[6]
          })
      else:
        first_line = False
  return render_template("Checkuser.html", users=users)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/usenow', methods=['GET'])
def usenow():
	
	return render_template('howyoudid.html')

class RegisterForm(Form):
	name = StringField('Name, [First Name Only]', [validators.Length(min=1, max=50)])
	musician = StringField('Musician (YES/NO)', [validators.Length(min=2, max=4)])
	instrument = StringField('If yes, Which Instrument?')
	years_of_exp = IntegerField('Years of experience (Only Number)')
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords do not match')
	])
	confirm = PasswordField('Confirm Password')
	consent = StringField('Consent to use your registration data and name? (YES/NO)', [validators.Length(min=2, max=4)])
	inst_of_record = StringField('Instrument you will use to tap the patterns? [Clapping, or any percussion instrument]')



@app.route('/login', methods=['GET', 'POST'])
def loggingin():
	error = None
	if request.method == 'POST':
		name = request.form['username']
		password = request.form['password']
		loging = confirm_login_pw(name,password)
		session['username'] = request.form['username']
		session['upload'] = 0
		if (loging):
			z = get_current_state(name)
			session['pattern'] = str(z[0][0])
			session['cycle'] = int(z[1][0])



			return redirect(url_for('learn'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')


@app.route('/dashboard/<int:n>', methods=['GET', 'POST'])
def dashboard(n):
	options = [4,3,5,7]
	cycle = session['cycle']
	name = session['username']
	pattern = session['pattern']
	#path = "static/Data/Users/"+name+"/results/errorplot"+str(pattern)+".png"
	#path = "../" + path
	path = session['plotpath']
	outname1='./static/Data/Users/'+name+'/results/temp'

	if os.path.exists(outname1):
		uppend_csv(str(pattern),str(cycle),str(name))
		session['upload'] = 0
	if request.method == 'POST':
		if (n==0):
			return redirect(url_for('learn', name=name))

		elif (n==1):
			if (pattern == '0111010'):
				path = "static/Data/Users/"+name+"/results/"
				files2 = os.listdir(path)
				files2.remove('results.csv')
				path2 = "../static/Data/Users/"+name+"/results/"
				for i in range(len(files2)):
					files2[i] = path2+files2[i]
					
				return render_template('howyoudid.html', name=name, files=files2)

			pro.filemanager(name,pattern)
			pattern,cyclelength = next_pattern(cycle,pattern)
			

			session['pattern'] = pattern
			filename = 'static/Data/Register.csv'
			df=pd.read_csv(filename,dtype={'Pattern':object})
			df[(df['Name']==name)]['CycleLength']=cyclelength
			df[(df['Name']==name)]['Pattern']=pattern
			session['cycle'] = cyclelength

			return redirect(url_for('learn', name=name))

	else:
		return render_template('dashboard.html', outPath = path, n=n)


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		userdata = dict(request.form)
		name = userdata["name"]
		musician = userdata["musician"]
		instrument = userdata["instrument"]
		years_of_exp = userdata["years_of_exp"]
		password = userdata["password"]
		Consent = userdata["consent"]
		InstrumentUsed = userdata["inst_of_record"]
		pattern = "1111"
		Cycle="4"
		newdir(name)
		create_csv(name)
		with open('static/Data/Users/Consent.csv', mode='a') as csv_file:
			data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			data.writerow([name,Consent, InstrumentUsed])

		with open('static/Data/Register.csv', mode='a') as csv_file:
			data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			data.writerow([name, musician, instrument, years_of_exp, password,pattern, Cycle])
		return redirect(url_for('loggingin'))
	return render_template('register.html', form=form)

if __name__ == '__main__':
	#host = '0.0.0.0',port = '8080'
	app.run()
	sslify = SSLify(app)
