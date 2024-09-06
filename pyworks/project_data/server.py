from flask import Flask

app = Flask(__name__) #Flask 클래스의 app 객체를 생성

# 웹 페이지의 경로 설정 라우팅
@app.route("/") # 루트 경로 127.0.0.1
def index(): #모든 사이트의 첫 페이지를 인덱스라고 함
    return "<p>Hello, World!</p>"

@app.route("/singup")
def singup():
    return "회원가입페이지"

@app.route("/shopping")
def shop():
    return "쇼핑 페이지입니다."

if __name__ == "__main__":
    app.run()