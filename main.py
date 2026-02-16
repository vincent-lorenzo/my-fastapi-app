from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Prime Checker Pro</title>
            <style>
                body { font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
                input { padding: 10px; border-radius: 5px; border: 1px solid #ccc; }
                button { padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
                .container { background: white; padding: 30px; display: inline-block; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Prime Checker!</h1>
                <p>Type a number to check if it is prime:</p>
                <input type="number" id="numInput" placeholder="Enter a number...">
                <button onclick="checkPrime()">Check Now</button>
                <h2 id="result"></h2>
            </div>

            <script>
                async function checkPrime() {
                    const num = document.getElementById('numInput').value;
                    const response = await fetch('/check-prime/' + num);
                    const data = await response.json();
                    const resultElement = document.getElementById('result');
                    if (data.is_prime) {
                        resultElement.innerText = "✅ " + num + " is a Prime Number!";
                        resultElement.style.color = "green";
                    } else {
                        resultElement.innerText = "❌ " + num + " is not prime.";
                        resultElement.style.color = "red";
                    }
                }
            </script>
        </body>
    </html>
    """

@app.get("/check-prime/{number}")
def check_prime(number: int):
    if number < 2:
        return {"number": number, "is_prime": False}
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return {"number": number, "is_prime": False}
    return {"number": number, "is_prime": True}