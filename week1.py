from flask import Flask,request,url_for,render_template,redirect
from flaskext.mysql import MySQL
app=Flask(__name__)
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='welcome123'
app.config['MYSQL_DATABASE_DB']='Akash_1'

mysql.init_app(app)
con=mysql.connect()
cur=con.cursor()
@app.route('/post_data')
def post_data():
	return render_template('post.html')
@app.route('/post',methods=['POST'])
def post():
	if request.method=='POST':
		book_id=request.form['ID']
		name=request.form['NAME']
		author=request.form['AUTHOR']
		published=request.form['YEAR']
		print("The book with the id "+book_id+" and name "+name+" was published by the author "+author+" in "+published+".")
		try:
			#t=time.clock()
			cur.execute('INSERT INTO data (ID,NAME,AUTHOR,YEAR) VALUES (%s,%s,%s,%s)',(book_id,name,author,published))
			con.commit()
			print('success')
			#print('Time taken for the execution '+time.clock()-t)
		except Exception as e:
			print(str(e))
		finally:
			return "SUCCESSFULLY ADDED"

@app.route('/update_data')
def update_data():
	return render_template('update.html')
@app.route('/updation',methods=['POST'])
def updation():
    if request.method == 'POST':
        book_id = request.form['ID']
        name = request.form['NAME']
        author = request.form['AUTHOR']
        published = request.form['YEAR']
        print(name)
        print(author)
        print(published)
        try:
           cur.execute('SELECT * from data where ID = %s', book_id)
           for row in cur:
               cur.execute('INSERT INTO table_2 (NAME,AUTHOR,YEAR) VALUES (%s, %s, %s)', (row[1], row[2], row[3]))
           query = 'UPDATE data SET NAME = %s, AUTHOR = %s, YEAR= %s where ID= %s'
           data = (name, author, published,book_id)
           cur.execute(query, data)
           con.commit()
           #con.close()
           print "Data fetched."
        except Exception as e:
           print(str(e))
           print ("Data not modified.")
        finally:
           return "SUCCESSFULLY UPDATED"


@app.route('/get_data')
def get_data():
	return render_template('get.html')

@app.route('/get',methods=['GET'])
def get():
	if request.method=='GET':
		book_id=request.args.get('ID')
		query='SELECT* from data where ID=%s'
		#t=time.clock()
		cur.execute(query,book_id)
		con.commit()
		m=''
		for row in cur:
			for j in range(len(row)):
				print(row[j])
				m=m+' '+ str(row[j])
		#print("Time taken to find the information was "+time.clock()-t)
		return m
@app.route('/delete_data')
def delete_data():
	return render_template('delete.html')

@app.route('/deletion',methods=['GET'])
def deletion():
	if(request.method=='GET'):
		book_id=request.args.get('ID')
		try:
			query='delete from data where id=%s'
			cur.execute(query,book_id)
			#print("Time taken for the deletion is "+ time.clock()-t)
			con.commit()
			print("Eureka!Book with the given id has been deleted from our database")
		except exception as e:
			print(str(e)+" ooops!We don't have the book with the given id")
		finally:
			return "DELECTED SUCCESSFULLY"


if __name__=='__main__':
	app.run(debug=True)



