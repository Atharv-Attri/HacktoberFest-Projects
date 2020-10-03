# Usage

The simplest usage is from a terminal: 
`
$ python christmas_tree.py 
       *
      ***
     *****
    *******
   *********
  ***********
      ***
     *****
    *******
   *********
  ***********
 *************
      ***       
      ***       
      ***       
      ***
`

The general idea for this was, though, to be used in a website, kind of as a quick thing you could do in flask and host in Heroku really quickly. In that case, you can use it programatically: 

`
from christmas_tree import make_random_tree

@app.route('/')
def home():
    """Landing page."""
    return render_template('home.html', tree=make_random_tree())
`

For usage of the other methods (`make_triangle()` and `make_tree()`), check the docstrings. 
