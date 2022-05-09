from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def entry_page():
    # template of the webpage
    return render_template('index.html')


@app.route('/predict_object/', methods=['GET', 'POST'])
def render_message():
    # Loading CNN model
    saved_model = 'conv.h5'
    model = load_model(saved_model)
    if request.method == 'POST':
        txt = request.form['txt']
        text = re.sub(r"http\S+", "", text)
        # Tokenize
        tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
        tokens = tokenizer.tokenize(text)
        # Remove non alphanumerica characters
        text = [word for word in tokens if word.isalpha()]
        return text

    try:

        # Call classify function to predict the image class using the loaded CNN model
        final, pred_class = classify(text, model)
        print(pred_class)
        print(final)

        # Store model prediction results to pass to the web page
        message = "Model prediction: {}".format(pred_class)
        print('Python module executed successfully')

    except Exception as e:
        # Store error to pass to the web page
        message = "Error encountered. Try another image. ErrorClass: {}, Argument: {} and Traceback details are: {}".format(
            e.__class__, e.args, e.__doc__)
        final = pd.DataFrame({'A': ['Error'], 'B': [0]})

    # Return the model results to the web page
    return render_template('index.html',
                           message=message)


# Debug is disabled for running in a jupyter notebook
app.run(debug=False)