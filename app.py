from flask import Flask, render_template

# 指定模板文件夹和静态文件夹的路径
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
