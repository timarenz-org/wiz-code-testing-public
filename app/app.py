from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)

# GET /download?file=../../etc/passwd
@app.route('/download')
def download_file():
    filename = request.args.get('file')
    return send_file(f'./files/{filename}')

@app.route('/execute')
def execute_command():
    user_input = request.args.get('input')
    sanitized_input = ''.join(c for c in user_input if c.isalnum())
    result = subprocess.run(['ls', sanitized_input], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)