import os

from flask import Flask, render_template, render_template_string, request

from utils import read_file

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message='Page not found')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', message='Internal server error')


@app.route('/')
@app.route('/<filename>')
def display_file(filename = 'file1.txt'):

    try:
        file_path = os.path.join(app.static_folder, filename)

        startline = int(request.args.get("start", 1))
        endline = int(request.args.get("end", -1))


        content = read_file(file_path, startline, endline)
        return render_template_string(content)

    except FileNotFoundError:
        return render_template('error.html', message=f'File "{filename}" not found')

    except UnicodeDecodeError as e:
        return render_template('error.html', message=f'Error decoding file "{filename}": {str(e)}')

    except Exception as e:
        return render_template('error.html', message=f'Error processing file "{filename}": {str(e)}')


if __name__ == "__main__":
    app.run(debug=True)
