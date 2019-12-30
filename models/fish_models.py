from xgboost import XGBClassifier
import numpy as np
import os


class PiscesModel:
    missing = -9999.0

    def __init__(self, species_id, properties, bmmi, iwi, wa, elevation, slope, threshold="crit_ave"):
        self.species_id = species_id
        self.properties = properties
        self.bmmi = bmmi
        self.iwi = iwi
        self.wa = wa
        self.elevation = elevation
        self.slope = slope
        self.threshold = threshold.lower()
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
        if self.threshold not in ["crit_ave", "crit_p1", "crit_1sd", "crit_p0", "crit_2sd"]:
            self.threshold = "crit_ave"

    def get_model_input(self):
        return [self.wa, self.elevation, self.bmmi, self.iwi, self.slope]

    def run_model(self, inputs):
        model = XGBClassifier()
        model_path = os.path.abspath('C:/git/qed_kube/data/app-data/pisces/Model_Files/Species_' + self.properties["model_id"])
        if not os.path.exists(model_path):
            model_path = os.path.abspath('./pisces_app/models/Model_Files/Species_' + self.properties["model_id"])
        model.load_model(model_path)
        pred = float(model.predict_proba(inputs)[:, 1])
        self.probability = round(100 * pred, 2)

    def get_prediction(self, threshold=None):
        threshold = str(threshold).lower()
        if threshold is None:
            threshold = self.threshold
        elif threshold not in ["crit_ave", "crit_p1", "crit_1sd", "crit_p0", "crit_2sd"]:
            threshold = self.threshold
        if self.probability <= self.properties[threshold]:
            prediction = 0
        else:
            prediction = 1
        return prediction
