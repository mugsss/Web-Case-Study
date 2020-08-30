from flask import Flask, render_template,url_for,request
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/addStudent')
def add():
	return render_template('add-student.html')


@app.route('/addStudent', methods = ['POST'])
def getValues():
	
	
	id1 = request.form['sid']
	name1 = request.form['name']
	gender1 = request.form['gender']
	dob1 = request.form['dob']
	city1 = request.form['city']
	state1 = request.form['state']
	email1 = request.form['email']
	quali1 = request.form['quali']
	stream1 = request.form['stream']
	if id1 == '' or  name1 == '' or dob1 == '' or gender1 == '' or  \
	city1 == '' or state1 == '' or email1 =='' or quali1 == '' or stream1 == '' :
		return render_template('add-student.html',\
			prediction_text="Some Fields are still Empty!!!!!")


	list1 = [id1,name1,gender1,dob1,city1,state1,email1,quali1,stream1]
	#print(list1)
	index = 0
	dataFile = open(r"C:\Users\Mugdha\Documents\LBJ_Project\data\addData.txt", "a")
	for data in list1:
		index = index+1
		dataFile.write(data)
		if index != (9):
			dataFile.write(', ')
		else:
			dataFile.write('\n')



	return render_template('add-student.html', \
		prediction_text2="Registration Successfull !!!!!!! ")

@app.route('/searchStudent')
def search1():
	return render_template('search-student.html')





@app.route('/studentFound', methods = ['POST'])
def found():
	id1 = request.form['sid']
	if id1 == '':
		return render_template('search-student.html',error1="Please enter ID!!")
	
	
	listFind = []
	fh = open(r"C:\Users\Mugdha\Documents\LBJ_Project\data\addData.txt",'r')
	for line in fh:
		x = line.split(",")
		listFind.append(x)
	#print(listFind)
	fh.close()
		
	listStudent = []
	headerList = listFind[0]
	for i in listFind:
	#print(i[0])
		x = str(id1)
		if(i[0]== x):
		#print("Hello")
			for details in i:
				listStudent.append(details)
			break;
			#listStudent[8] = listStudent[8][:-1]
	if not listStudent:
		return render_template('search-student.html', \
			error2="Record with StudentID: {} not found!!".format(id1))

	studentDict = dict(zip(headerList, listStudent))
	return render_template('found-student.html', \
	 dict1 = studentDict, success ="Student record found!!!")




@app.route('/displayStudent')
def dis():
	listFind = []
	fh = open(r"C:\Users\Mugdha\Documents\LBJ_Project\data\addData.txt",'r')
	for line in fh:
		x = line.split(",")
		listFind.append(x)
	#print(listFind)
	fh.close()
	
	x = len(listFind)
	headerS=listFind[0]
	return render_template("display-students.html",\
		listDisplay = listFind, len1 = x , headerS = headerS)	
				
if __name__ == "__main__":
	app.run(debug=True)