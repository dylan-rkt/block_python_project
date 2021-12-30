import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def target(request):
    init_model()
    x_values = to_x_values(request)
    return predict_class(x_values)

def to_x_values(request):
    values = request.POST

    height = int(values['height'])
    length = int(values['length'])
    blackpix = int(values['blackpix'])
    blackand = int(values['blackand'])
    wb_trans = int(values['wb_trans'])
    area = height * length
    eccen = length / height
    p_black = blackpix / area
    p_and = blackand / area
    mean_tr = blackpix / wb_trans

    return scaler.transform([[height, length, area, eccen, p_black, p_and, mean_tr, blackpix, blackand, wb_trans]])

def init_model():
    global rfc
    global scaler
    data = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '\\page-blocks.data', delimiter="\s+", header=None)
    columns = ['height', 'length', 'area', 'eccen', 'p_black', 'p_and', 'mean_tr', 'blackpix', 'blackand', 'wb_trans',
               'class']
    data.columns = columns
    labels = data['class']

    scaler = StandardScaler()
    scaler.fit(data[data.columns[:-1]])
    data_scaled = scaler.transform(data[data.columns[:-1]])
    data_scaled = pd.DataFrame(data_scaled)
    data_scaled.columns = columns[:-1]
    data_scaled['class'] = data['class']

    x = data_scaled[data_scaled.columns[:-1]]
    y = data_scaled[data_scaled.columns[-1]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    rfc = RandomForestClassifier(criterion='entropy', min_weight_fraction_leaf=0,
                                 n_estimators=50)
    rfc.fit(x_train, y_train)

def predict_class(x_values):
    return rfc.predict(x_values)


