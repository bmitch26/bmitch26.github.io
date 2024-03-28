# Holds the flask and backend logic
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    
with app.app_context():
    db.create_all()
    
@app.route('/')
def index():
    comments = Comment.query.all()
    return render_template('index.html', comments=comments)

@app.route('/post', methods=['POST'])
def post_comment():
    comment_content = request.form['content']
    new_comment = Comment(content=comment_content)
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()