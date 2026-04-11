import matplotlib.pyplot as plt
from flask import Flask, request, render_template_string

app = Flask(__name__)

# COMPUTER NETWORKS (CN)
def get_traffic_weight(level):
    if level == "low":
        return 1
    elif level == "medium":
        return 2
    elif level == "high":
        return 3
    return 1

# OPERATING SYSTEM
class Signal:
    def __init__(self, road, weight):
        self.road = road
        self.weight = weight
        self.green_time = 0

# ANALYSIS OF ALGORITHMS (AOA)
def priority_scheduling(signals):
    signals.sort(key=lambda x: x.weight, reverse=True)
    for s in signals:
        s.green_time = s.weight * 10
    return signals

# WEB INTERFACE
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart Traffic Signal Management</title>
    <style>
        body { font-family: Arial; padding: 25px; }
        select, button { padding: 6px; margin: 6px; }
    </style>
</head>
<body>

<h2>🚦 Smart Traffic Signal Management System</h2>
<p>This system dynamically allocates green signal time based on traffic density.</p>

<form method="post">
    <p>Road A:
        <select name="a">
            <option>low</option>
            <option>medium</option>
            <option>high</option>
        </select>
    </p>

    <p>Road B:
        <select name="b">
            <option>low</option>
            <option>medium</option>
            <option>high</option>
        </select>
    </p>

    <p>Road C:
        <select name="c">
            <option>low</option>
            <option>medium</option>
            <option>high</option>
        </select>
    </p>

    <p>Road D:
        <select name="d">
            <option>low</option>
            <option>medium</option>
            <option>high</option>
        </select>
    </p>

    <button type="submit">Generate Signal Timing</button>
</form>

{% if result %}
<hr>
<h3>📊 Signal Scheduling Output</h3>
<ul>
{% for s in result %}
    <li><b>{{ s.road }}</b> → Green Time: {{ s.green_time }} seconds</li>
{% endfor %}
</ul>

<h3>📈 Traffic Analysis Graph</h3>
<img src="/static/traffic.png" width="450">
{% endif %}

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        roads = ["Road A", "Road B", "Road C", "Road D"]
        levels = [
            request.form["a"],
            request.form["b"],
            request.form["c"],
            request.form["d"]
        ]

        signals = []
        for road, level in zip(roads, levels):
            weight = get_traffic_weight(level)
            signals.append(Signal(road, weight))

        result = priority_scheduling(signals)

        # Graph generation
        names = [s.road for s in result]
        times = [s.green_time for s in result]

        plt.bar(names, times)
        plt.xlabel("Road")
        plt.ylabel("Green Time (seconds)")
        plt.title("Smart Traffic Signal Scheduling")
        plt.savefig("static/traffic.png")
        plt.close()

    return render_template_string(HTML_PAGE, result=result)


if __name__ == "__main__":
    app.run(debug=True)
