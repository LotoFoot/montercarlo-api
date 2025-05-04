from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)

chevaux = {
    "Dinasty": {"moyenne": 72, "ecart_type": 2},
    "Lady_Nerud": {"moyenne": 73, "ecart_type": 2.5},
    "Macanudassa": {"moyenne": 74, "ecart_type": 3},
    "Oliver_Twist": {"moyenne": 75, "ecart_type": 2.5},
    "Quincy_Jones": {"moyenne": 76, "ecart_type": 3}
}

def monte_carlo_simulation(chevaux, n_simulations=10000):
    top3_counts = {cheval: 0 for cheval in chevaux}
    for _ in range(n_simulations):
        temps_sim = {cheval: np.random.normal(data["moyenne"], data["ecart_type"]) for cheval, data in chevaux.items()}
        classement = sorted(temps_sim.items(), key=lambda x: x[1])
        for cheval, _ in classement[:3]:
            top3_counts[cheval] += 1
    probabilites = {cheval: count / n_simulations * 100 for cheval, count in top3_counts.items()}
    return probabilites

@app.route('/simulate', methods=['GET'])
def simulate():
    n = int(request.args.get('n', 10000))
    result = monte_carlo_simulation(chevaux, n)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

