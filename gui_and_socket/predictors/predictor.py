class Predictor:
    def __init__(self, sequence):
        self.sequence = sequence
        self.calculated = []
        print('Sequence loaded')

    def calculate(self):
        pass # Store result in self.calculated in form [aa1_prediction, aa2_prediction, aa3_prediction, ...]

    def get_value_for_AA(self, aa_index):
        return self.calculated[aa_index]

    def get_weighted_value_for_AA(self, aa_index, weight = 1):
        return self.calculated[aa_index] * weight

    def get_all_values(self):
        return self.calculated

    def get_all_weighted_values(self, weight):
        return [weight * aa for aa in self.calculated]