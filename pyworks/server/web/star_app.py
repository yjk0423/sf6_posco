from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')
    # return "메인페이지 입니다."
@app.route('/season')
def get_season():
    season = "여름"
    seasons = ["봄","여름","가을","겨울"]
    return  render_template('season.html', season=season,seasons=seasons)
@app.route('/loop')
def loop():
    items = ['a','b','c','d']
    return render_template('loop.html', item=items)

@app.route('/calculate', methods=['GET', 'POST']) # methods type 대문자로 해야함 소문자 안먹음;
def calc():
    if request.method == 'POST':
        try :
        # 폼에 입력된 글자는 str임
            num = int(request.form['num'])
        except ValueError:
            err_msg = "정수를 입력하세요."
            return render_template('calculate.html',err_msg=err_msg)
        else:
            if num % 2 == 0:
                result = "짝수입니다."
            else:
                result = "홀수입니다."
            return render_template('calc_result.html', result=result)

    else:
        return render_template('calculate.html')

if __name__ == "__main__":
    app.run(debug=True)
