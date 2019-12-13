from xgboost import XGBClassifier
import numpy as np
import pandas
import os


species_data = pandas.read_csv(os.path.abspath('./pisces_app/models/pythonmodelstats.csv'), index_col=1, skiprows=0).T.to_dict()


class PiscesModel:
    missing = -9999.0

    def __init__(self, species_id, bmmi, iwi, wa, elevation, slope, threshold="Crit_Ave"):
        self.species_id = species_id
        self.bmmi = bmmi
        self.iwi = iwi
        self.wa = wa
        self.elevation = elevation
        self.slope = slope
        self.threshold = threshold
        self.validate_inputs()
        self.probability = None
        self.run_model(self.get_model_input())

    def validate_inputs(self):
        if self.bmmi == self.missing:
            self.bmmi = np.NaN
        if self.iwi == self.missing:
            self.iwi = np.NaN
        if self.wa == self.missing:
            self.wa = np.NaN
        if self.elevation == self.missing:
            self.elevation = np.NaN
        if self.slope == self.missing:
            self.slope = np.NaN
        if self.threshold not in ["Crit_Ave", "Crit_P1", "Crit_1SD", "Crit_P0", "Crit_2SD"]:
            self.threshold = "Crit-Ave"

    def get_model_input(self):
        return [self.wa, self.elevation, self.bmmi, self.iwi, self.slope]

    def run_model(self, inputs):
        model = XGBClassifier()
        model_path = os.path.abspath('./pisces_app/models/Model_Files/Species_' + str(species_data[self.species_id]["Model"]))
        model.load_model(model_path)
        pred = float(model.predict_proba(inputs)[:, 1])
        self.probability = round(100 * pred, 2)

    def get_prediction(self, threshold=None):
        if threshold is None:
            threshold = self.threshold
        elif threshold not in ["Crit_Ave", "Crit_P1", "Crit_1SD", "Crit_P0", "Crit_2SD"]:
            threshold = self.threshold
        if self.probability <= float(species_data[self.species_id][threshold]):
            prediction = 0
        else:
            prediction = 1
        return prediction


def check_properties(species_id):
    if species_id in species_data.keys():
        return True
    else:
        return False
