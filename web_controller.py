from flask import Flask, render_template_string
from gpiozero import Motor

app = Flask(__name__)

# Configure motors (matching your working setup)
left_motor = Motor(forward=13, backward=19)
right_motor = Motor(forward=18, backward=12)  # Inverted right motor

# Simple HTML Control Panel with embedded CSS/JS
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Lawnmower Remote</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background: #222; color: #fff; margin-top: 50px; }
        h1 { color: #4CAF50; }
        .btn { font-size: 20px; padding: 20px 40px; margin: 10px; cursor: pointer; border: none; border-radius: 10px; background-color: #4CAF50; color: white; width: 150px; }
        .btn:active { background-color: #45a049; }
        .stop-btn { background-color: #f44336; }
        .stop-btn:active { background-color: #da190b; }
        .grid { display: flex; flex-direction: column; align-items: center; }
    </style>
</head>
<body>
    <h1>Lawnberry Pi RC</h1>
    <div class="grid">
        <button class="btn" onclick="sendCommand('forward')">FORWARD</button>
        <div>
            <button class="btn" onclick="sendCommand('left')">LEFT</button>
            <button class="btn stop-btn" onclick="sendCommand('stop')">STOP</button>
            <button class="btn" onclick="sendCommand('right')">RIGHT</button>
        </div>
        <button class="btn" onclick="sendCommand('backward')">BACKWARD</button>
    </div>

    <script>
        function sendCommand(cmd) {
            fetch('/move/' + cmd).then(response => response.text()).then(data => console.log(data));
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/move/<direction>')
def move(direction):
    speed = 0.4  # 40% speed for safety on workbench
    if direction == 'forward':
        left_motor.forward(speed)
        right_motor.forward(speed)
    elif direction == 'backward':
        left_motor.backward(speed)
        right_motor.backward(speed)
    elif direction == 'left':
        left_motor.backward(speed)
        right_motor.forward(speed)
    elif direction == 'right':
        left_motor.forward(speed)
        right_motor.backward(speed)
    elif direction == 'stop':
        left_motor.stop()
        right_motor.stop()
    return f"Executed: {direction}"

if __name__ == '__main__':
    # Runs on port 5000, accessible from any device on your Wi-Fi network
    app.run(host='0.0.0.0', port=5000, debug=False)
