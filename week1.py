from flask import Flask,request,url_for
from flaskext.mysql import MySQL
app=Flask(__name__)
mysql=MySQL()
app.config['MYSQL_DATABASE_USER']='akash'
app.config['MYSQL_DATABASE_PASSWORD']='welcome123'
app.config['MYSQL_DATABASE_DB']='publications'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)
con=mysql.connect()
cur=con.cursor()

@app.route('/post/',methods=['POST'])
def post():
	if request.method=='POST':
		book_id=request.form['id']
		name=request.form['name']
		author=request.form['author']
		published=request.form['year']
		print("The book with the id "+book_id+" and name "+name+" was published by the author "+author+" in "+published+".")
		try:
			query='INSERT INTO data (book_id,name,author,published VALUES (%d,%s,%s,%d)'
			t=time.clock()
			cur.execute(query,(book_id,name,author,published))
			print("Time taken for execution is "+time.clock()-t)
			con.commit()
			print("SUCCESS")
		except EXCEPTION as e:
			print(str(e)+":FAILURE")
		finally:
			return redirect('/',200)

@app.route('/update/',methods=['POST'])
def updation():
	if request.method=='POST':
		book_id=request.form['id']
		name=request.form['name']
		author=request.form['author']
		published=request.form['year']
		print("Update the book with the id "+book_id+" with name "+name+" as it published by the author "+author+" in "+published+".")
		try:
			query='SELECT * from data where book_id=%d'
			t=time.clock()
			cur.execute(query,book_id)
			query='INSERT INTO table_2 (name,author,published) values (%s,%s,%d)'
			cur.execute(query,(cur[1],cur[2],cur[3]))
			query='UPDATE data set name=%s,author=%s,published=%d where book_id=%d'
			cur.execute(query,(book_id,name,author,published))
			print("Time take for updating is "+time.clock()-t)
			con.commit();
			print("Eureka!Your database has been updated")
		except Exception as e:
			print(Str(e)+" Sorry it can't be updated.We are facing some issues so try later")
		finally:
		    return redirect(url_for('home'))

@app.route('/',methods=['GET'])
def home():
	print("Welcome to this database")

@app.route('/find/',methods=['GET'])
def get():
	if request.method=='GET':
		book_id=request.args.get('id')
		try:
			query='SELECT from data where book_id=%d'
			t=time.execute()
			cur.execute(query,book_id)
			print("Name of the book with the id "+book_id+" is "+cur[1]+" whose author is "+cur[2]+" which was published in "+cur[3])
			print("Time taken to find the information was "+time.clock()-t)
			con.commit()
		except exception as e:
			print(str(e)+" We don't have any data with the given book_id")
		finally:
			return (redirect(url_for('home')))


@app.route('/delete/',methods=['GET'])
def deletion():
	if(request.method=='GET'):
		book_id=request.args.get('id')
		try:
			query='SELECT* from data where book_id=%d'
			t=time.clock()
			cur.execute(query,book_id)
			query='INSERT INTO table_2(name,author,published) values (%s ,%s,%d)'
			cur.execute(query,(cur[1],cur[2],cur[3]))
			query='delete from data where book_id=%d'
			cur.execute(query,book_id)
			print("Time taken for the deletion is "+ time.clock()-t)
			con.commit()
			print("Eureka!Book with the given id has been deleted from our database")
		except exception as e:
			print(str(e)+" ooops!We don't have the book with the given id")
		finally:
			return redirect(url_for('home'))


if __name__==__main__:
	app.run(debug=True)



