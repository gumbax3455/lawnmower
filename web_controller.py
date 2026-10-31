from flask import Flask, render_template_string, request
from gpiozero import Motor

app = Flask(__name__)

# Configure motors (matching your working setup with inverted right motor)
left_motor = Motor(forward=13, backward=19)
right_motor = Motor(forward=18, backward=12)

# HTML Control Panel with Speed Slider and no headline
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Lawnmower Remote</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background: #222; color: #fff; margin-top: 40px; }
        .btn { font-size: 20px; padding: 20px 40px; margin: 10px; cursor: pointer; border: none; border-radius: 10px; background-color: #4CAF50; color: white; width: 150px; }
        .btn:active { background-color: #45a049; }
        .stop-btn { background-color: #f44336; }
        .stop-btn:active { background-color: #da190b; }
        .grid { display: flex; flex-direction: column; align-items: center; }
        .slider-container { margin: 25px; background: #333; padding: 15px; border-radius: 10px; display: inline-block; }
        input[type=range] { width: 250px; height: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="grid">
        <div class="slider-container">
            <label for="speedSlider">Speed: <span id="speedVal">40</span>%</label><br><br>
            <input type="range" id="speedSlider" min="10" max="100" value="40" 
                   oninput="document.getElementById('speedVal').innerText = this.value">
        </div>

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
            let sliderVal = document.getElementById('speedSlider').value;
            let speed = sliderVal / 100.0;  // Convert percentage to 0.0 - 1.0 scale
            
            fetch('/move/' + cmd + '?speed=' + speed)
                .then(response => response.text())
                .then(data => console.log(data));
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
    # Get speed parameter from URL query string, default to 40% (0.4)
    speed = request.args.get('speed', default=0.4, type=float)
    speed = max(0.0, min(1.0, speed))  # Safety bounds clamp
    
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
        
    return f"Executed: {direction} at speed {speed:.2f}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
