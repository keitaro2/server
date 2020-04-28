from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
port_num = 16074

@app.route('/', methods=['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/humidsensor', methods=['POST'])
def update_humidsensor():
    time = request.form["time"]
    h = request.form["humid"]
    t = request.form["temp"]
    try:
        f = open(file_path, 'w')
        f.write(time + "," + h + "," + t)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

@app.route('/humidsensor', methods=['GET'])
def get_humidsensor():
    try:
        f = open(file_path, 'r')
        for row in f:
            humidsensor = row
    except Exception as e:
        print(e)
        return e
    finally:
        f.close()
        return humidsensor

if __name__ == '__main__':
    print("a")
    app.run(debug=True, host='0.0.0.0', port=port_num)
