from flask import Flask, request, session, redirect, url_for, render_template, flash

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    gcd_result = gcd(a, b)
    return (gcd_result, a * b // gcd_result)

def calc(num1, num2):
    return lcm(num1, num2)

# http://127.0.0.1:5000 にアクセスしたときに実行されるメソッド
@app.route('/')
def toppage():
    # toppage.htmlを表示する
    return render_template('toppage.html')

# post形式で/calcが呼ばれたときに実行されるメソッド
@app.route('/calc', methods=['POST'])
def login():
    # request.formで値を受け取る
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    gcd, lcm = calc(num1, num2)
    # numをresult.htmlに送る
    return render_template('result.html', num1=num1, num2=num2, gcd=gcd, lcm=lcm)

if __name__ == '__main__':
    app.run()
