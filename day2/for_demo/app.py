from flask import Flask,render_template

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})

@app.route('/')
def hello_world():
    context ={
       'users':['test1','test2','test3'],
        'person':{
            'username':'kangbazi',
            'age':18,
            'country':'china'
        },
        'books':[
            {
               'name':'三国演义',
                'author':'罗贯中',
                'price':10
            },
            {
                'name': '金瓶梅',
                'author': '笑笑生',
                'price': 100
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 20
            }
        ]
    }
    return render_template('index.html',**context)


if __name__ == '__main__':
    app.run(port=5001)
