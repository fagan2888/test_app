from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('jobs_vs_prices.html')


@app.route('/jobs_vs_prices', methods=['POST'])
def jobs_vs_prices():
    return render_template('jobs_vs_prices_graph.html')
	
if __name__ == "__main__":
	app.run()