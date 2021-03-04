import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import model_from_json


class Demo:
    def __init__(self, mode, models_path, data_path, day_or_week=0):
        if mode not in ["daily_forecasting", "weekly_forecasting"]:
            raise Exception(f"'{mode}' mode is nos supported")

        self.mode = mode
        self.models_path = os.path.join(models_path, mode)
        self.data_path = data_path
        self.day_or_week = day_or_week
        self.scaler = None
        self.model = None
        self.test_data = None

    @staticmethod
    def split_sequence(sequence, n_steps_in, n_steps_out):
        x, y = list(), list()
        for i in range(len(sequence)):
            end_ix = i + n_steps_in
            out_end_ix = end_ix + n_steps_out
            if out_end_ix > len(sequence):
                break
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix:out_end_ix]
            x.append(seq_x)
            y.append(seq_y)

        return np.array(x), np.array(y)

    def __load_data(self, in_time_steps, out_time_steps):
        data = pd.read_csv(self.data_path)

        # Scale the data
        data = np.array(data)
        self.scaler = StandardScaler().fit(data.reshape(-1, 1))
        data = self.scaler.transform(data.reshape(-1, 1))
        data = data.ravel()
        self.test_data = data[148920:]

        # Test data
        x, y = self.split_sequence(self.test_data, in_time_steps, out_time_steps)

        x = x[self.day_or_week]
        x = x.reshape((1, x.shape[0], 1))
        y = y[self.day_or_week]

        return x, y

    def __load_model(self):
        files = os.listdir(self.models_path)

        json_filepath = None
        h5_filepath = None

        for file in files:
            if str(file).endswith(".json"):
                json_filepath = os.path.join(self.models_path, file)
            elif str(file).endswith(".h5"):
                h5_filepath = os.path.join(self.models_path, file)
            else:
                raise Exception("The .json and/or .h5 model file is missing.")

        json_file = open(json_filepath)
        json_data = json_file.read()
        json_file.close()

        self.model = model_from_json(json_data)
        self.model.load_weights(h5_filepath)

        pass

    def __predict(self, x):
        y_hat = self.model.predict(x, verbose=0)
        y_hat = self.scaler.inverse_transform(y_hat)
        y_hat = y_hat.reshape(-1)

        return y_hat

    def __plot(self, y_true, y_hat):
        raw_test_data = self.scaler.inverse_transform(self.test_data)
        y_true = self.scaler.inverse_transform(y_true)

        hist = raw_test_data[self.day_or_week - 48:self.day_or_week]
        hist = np.hstack((hist, y_true))

        time = range(48, 48 + y_hat.shape[0])

        plt.figure(figsize=(7, 5))
        plt.plot(hist, 'r', label='Actual', linewidth=1)
        plt.plot(time, y_hat, 'b--', label='Predict', linewidth=1)
        plt.legend(loc='upper left', fontsize=8)
        plt.xlabel("Time [hours]", fontsize=12)
        plt.ylabel("GHI $[kWh/m^2]$", fontsize=12)
        plt.grid(True)
        plt.yticks(size=8)
        plt.xticks(size=8)
        plt.show()

        pass

    def __get_metrics(self, y_true, y_hat):
        y_true = self.scaler.inverse_transform(y_true)

        rms_e = np.sqrt(mean_squared_error(y_true, y_hat))
        mae = mean_absolute_error(y_true, y_hat)
        r2 = r2_score(y_true, y_hat)

        return rms_e, mae, r2

    def run(self):
        print("Loading data...")
        x, y = None, None
        if self.mode == "daily_forecasting":
            x, y = self.__load_data(in_time_steps=168, out_time_steps=24)
        elif self.mode == "weekly_forecasting":
            x, y = self.__load_data(in_time_steps=672, out_time_steps=168)

        print("Loading model...")
        self.__load_model()

        print("Predicting data...")
        y_hat = self.__predict(x)

        self.__plot(y, y_hat)
        mse_r, mae, r2 = self.__get_metrics(y, y_hat)
        print("---------------------------")
        print("----------RESULTS----------")
        print("---------------------------")
        print(f"MSER:   {mse_r}")
        print(f"MAE:    {mae}")
        print(f"R2:     {mse_r}")
        print("---------------------------")

        return True
