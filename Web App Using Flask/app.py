from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
posts = {
    0:{
        'title':'Hello Guys',
        'content': 'This is my First Flask App.'
    }
}
"""
@app.route('/')  # route of website
def home():
    return 'Hello Vishal'
"""


# Our Nice Home Page

@app.route('/')
def home():
    return render_template('home.jinja2', posts=posts)

    
"""
@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    #return f"Post: {post['title']}, Content: {post['content']}"
    #return render_template('post.html')
    #return render_template('post2.html', dict=post)
    if not post: # if post is none=true and not none=false
        return render_template('404.html', message=f'Your Entered Post Id {post_id} Was Not Found')
    return render_template('post.html')

if __name__ == "__main__":
    app.run(debug=True)

"""

"""
jinja2:- Jinja2 is a web template engine which combines a template
with a certain data source to render the dynamic web pages.
"""

# for jinja2 files


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    #return f"Post: {post['title']}, Content: {post['content']}"
    #return render_template('post.html')
    #return render_template('post2.html', dict=post)
    if not post: # if post is none=true and not none=false
        return render_template('404child.jinja2', message=f'Your Entered Post Id {post_id} Was Not Found')
    return render_template('postchild.jinja2', post=post)
"""
@app.route('/post/form')
def form():
    return render_template('createform.jinja2')

# This route will be arrived at looking like this:
# 127.0.0.1:5000/post/create
# It will also have some inner data as part of the payload (which is hidden),containing the data in the form.
@app.route('/post/create', methods=['POST'])
def create():
    title = request.form.get('title') # This takes the 'Hello' from the form contents.
    content = request.form.get('content')  # This takes the 'This is the post content' form the form contents.
    post_id = len(posts)
    posts[post_id] = {'id_no': post_id, 'title': title, 'content': content}
    return redirect(url_for('post', post_id=post_id))
"""

# We can Simplify Our Code By Using GET in method.

@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title') # This takes the 'Hello' from the form contents.
        content = request.form.get('content')  # This takes the 'This is the post content' form the form contents.
        post_id = len(posts)
        posts[post_id] = {'id_no': post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id))
    return render_template('createform.jinja2')

if __name__ == "__main__":
    app.run(debug=True)




