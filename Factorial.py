from flask import Flask, request

app = Flask(__name__)

@app.route("/factorial/<int:n>", methods =["GET"])
def factorial(n):
  r = calculate(n)
  return {"result":r},200

def calculate(n):
  total = 1
  for i in range(0,n-1):
    total = total * (n-i)

  return total

if __name__ == "__main__":
  app.run(host="localhost",port=7000)

