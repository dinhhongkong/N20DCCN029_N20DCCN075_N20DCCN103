import numpy as np
import pandas as pd
from tkinter import ttk
import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
import pickle


with open('GRADIENT_BOOSTING_MODEL.pkl', 'rb') as f:
    model_gbm = pickle.load(f)


def get_unique_values(column_name, data):
    dt = data[column_name].unique()
    values = [value for value in dt.tolist()]
    values = sorted(values)
    return values


numericalFeatures = ['no_of_adults', 'no_of_children', 'no_of_week_nights',
                     'no_of_week_nights', 'lead_time', 'arrival_date',
                     'no_of_previous_cancellations', 'no_of_previous_bookings_not_canceled',
                     'avg_price_per_room']

categoricalFeatures = ['type_of_meal_plan', 'required_car_parking_space',
                       'no_of_special_requests', 'room_type_reserved', 'arrival_year',
                       'arrival_month', 'market_segment_type', 'repeated_guest']


def LabelEncoding(X, features=categoricalFeatures):
    le = LabelEncoder()
    for i in features:
        X[i] = le.fit_transform(X[i])
    return X


class Gradient_Boosting_GUI:

    def __init__(self, master):
        self.master = master
        master.title("Gradient Boosting Demo")

        self.data = pd.read_csv('Hotel Reservations.csv')

        self.no_of_adults_box = self.create_combobox(
            "Number of adults", get_unique_values("no_of_adults", self.data))
        self.no_of_children_box = self.create_combobox(
            "Number of children", get_unique_values("no_of_children", self.data))
        self.no_of_weekend_nights_box = self.create_combobox(
            "Number of weekend nights", get_unique_values("no_of_weekend_nights", self.data))
        self.no_of_week_nights_box = self.create_combobox(
            "Number of week nights", get_unique_values("no_of_week_nights", self.data))
        self.type_of_meal_plan_box = self.create_combobox(
            "Type of meal plan", get_unique_values("type_of_meal_plan", self.data))
        self.required_car_parking_space_box = self.create_combobox(
            "Required car parking space", get_unique_values("required_car_parking_space", self.data))
        self.room_type_reserved_box = self.create_combobox(
            "Room type reserved", get_unique_values("room_type_reserved", self.data))
        self.lead_time_box = self.create_combobox(
            "Lead time", get_unique_values("lead_time", self.data))
        self.arrival_year_box = self.create_combobox(
            "Arrival year", get_unique_values("arrival_year", self.data))
        self.arrival_month_box = self.create_combobox(
            "Arrival month", get_unique_values("arrival_month", self.data))
        self.arrival_date_box = self.create_combobox(
            "Arrival date", get_unique_values("arrival_date", self.data))
        self.market_segment_type_box = self.create_combobox(
            "Market segment type", get_unique_values("market_segment_type", self.data))
        self.repeated_guest_box = self.create_combobox(
            "Repeated guest", get_unique_values("repeated_guest", self.data))
        self.no_of_previous_cancellations_box = self.create_combobox(
            "Number of previous Cancellations", get_unique_values("no_of_previous_cancellations", self.data))
        self.no_of_previous_bookings_not_canceled_box = self.create_combobox(
            "Number of previous booking not canceled", get_unique_values("no_of_previous_bookings_not_canceled", self.data))
        self.avg_price_per_room_box = self.create_combobox(
            "Average price per room", get_unique_values("avg_price_per_room", self.data))
        self.no_of_special_requests_box = self.create_combobox(
            "Number of special requests", get_unique_values("no_of_special_requests", self.data))

        self.predict_button = tk.Button(
            master, text="Predict", command=self.predict_class)
        self.predict_button.pack()

        self.prediction_label = tk.Label(master, text="", padx=200, pady=10)
        self.prediction_label.pack()

    def create_combobox(self, label_text, values):
        frame = tk.Frame(self.master, padx=10, pady=5)
        frame.pack(side=tk.TOP)

        label = tk.Label(frame, text=label_text, padx=10,
                         pady=3, width=35, anchor='w')
        label.pack(side=tk.LEFT, padx=(0, 5))

        combobox = ttk.Combobox(frame, values=values)
        combobox.pack(side=tk.RIGHT, padx=5, pady=5)
        return combobox

    def predict_class(self):
        # ẩn label đã dự đoán trước đó
        self.prediction_label.config(text="Prediction: ")
        # Lấy giá trị của các combobox

        no_of_adults = self.no_of_adults_box.get()
        no_of_children = self.no_of_children_box.get()
        no_of_weekend_nights = self.no_of_weekend_nights_box.get()
        no_of_week_nights = self.no_of_week_nights_box.get()
        type_of_meal_plan = self.type_of_meal_plan_box.get()
        required_car_parking_space = self.required_car_parking_space_box.get()
        room_type_reserved = self.room_type_reserved_box.get()
        lead_time = self.lead_time_box.get()
        arrival_year = self.arrival_year_box.get()
        arrival_month = self.arrival_month_box.get()
        arrival_date = self.arrival_date_box.get()
        market_segment_type = self.market_segment_type_box.get()
        repeated_guest = self.repeated_guest_box.get()
        no_of_previous_cancellations = self.no_of_previous_cancellations_box.get()
        no_of_previous_bookings_not_canceled = self.no_of_previous_bookings_not_canceled_box.get()
        avg_price_per_room = self.avg_price_per_room_box.get()
        no_of_special_requests = self.no_of_special_requests_box.get()

        # Tạo dataframe chứa dữ liệu người dùng nhập
        input_data = pd.DataFrame({'no_of_adults': [no_of_adults],
                                   'no_of_children': [no_of_children],
                                   'no_of_weekend_nights': [no_of_weekend_nights],
                                   'no_of_week_nights': [no_of_week_nights],
                                   'type_of_meal_plan': [type_of_meal_plan],
                                   'required_car_parking_space': [required_car_parking_space],
                                   'room_type_reserved': [room_type_reserved],
                                   'lead_time': [lead_time],
                                   'arrival_year': [arrival_year],
                                   'arrival_month': [arrival_month],
                                   'arrival_date': [arrival_date],
                                   'market_segment_type': [market_segment_type],
                                   'repeated_guest': [repeated_guest],
                                   'no_of_previous_cancellations': [no_of_previous_cancellations],
                                   'no_of_previous_bookings_not_canceled': [no_of_previous_bookings_not_canceled],
                                   'avg_price_per_room': [avg_price_per_room],
                                   'no_of_special_requests': [no_of_special_requests]})
        input_data = LabelEncoding(input_data)
        print(input_data)
        self.Y_pred = model_gbm.predict(input_data)
        print(self.Y_pred)
        if (self.Y_pred == 0):
            prediction = "Canceled"
        else:
            prediction = "Not canceled"
        # Hiển thị kết quả dự đoán lên giao diện
        self.prediction_label.config(text="Prediction: " + str(prediction))


if __name__ == "__main__":
    root = tk.Tk()
    # Lấy kích thước màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Thiết lập kích thước của cửa sổ
    root.geometry(f"{screen_width}x{screen_height}")

    gradient_boosting_gui = Gradient_Boosting_GUI(root)
    root.mainloop()
