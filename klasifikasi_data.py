import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.neural_network import MLPClassifier
import os

def app():
    st.header("🧮 Klasifikasi Data 🧮")

    # Fitur untuk mengunggah data (wajib)
    st.sidebar.header("Unggah Data yang Sudah Diproses")
    upload_data = st.sidebar.file_uploader("Pilih file CSV yang sudah diproses:", type=["csv"])

    # Jika data diunggah
    if upload_data is not None:
        # Membaca file yang diunggah dan menyimpannya di session_state
        data = pd.read_csv(upload_data)
        st.session_state['data'] = data
        st.success("Data berhasil diunggah.")

        # Pilih fitur dan target
        st.sidebar.header("Pengaturan Klasifikasi")
        feature_columns = st.sidebar.multiselect(
            "Pilih Kolom Fitur:", options=data.columns, default=data.columns[:-1]
        )

        # Memperbaiki pengaturan untuk kolom target, bisa pilih selain kolom fitur
        target_column = st.sidebar.selectbox(
            "Pilih Kolom Target:", 
            options=[col for col in data.columns if col not in feature_columns]
        )

        # Menampilkan kolom fitur dan target yang dipilih
        st.write(f"Fitur yang dipilih: {feature_columns}")
        st.write(f"Kolom Target yang dipilih: {target_column}")

        # Pilih model untuk klasifikasi
        model_algorithm = st.sidebar.selectbox(
            "Pilih Algoritma Model:", 
            options=["Random Forest", "XGBoost", "Neural Network"]
        )

        if feature_columns and target_column:
            X = data[feature_columns]
            y = data[target_column]

            # Preprocessing hanya diperlukan jika data belum diproses
            label_enc = LabelEncoder()
            y = label_enc.fit_transform(y)

            # Separate numeric and non-numeric columns
            numeric_columns = X.select_dtypes(include=['number']).columns
            categorical_columns = X.select_dtypes(exclude=['number']).columns

            # Handle missing values in numeric columns
            imputer = SimpleImputer(strategy='mean')
            X[numeric_columns] = imputer.fit_transform(X[numeric_columns])

            # Handle categorical columns (if any) by encoding them
            for col in categorical_columns:
                X[col] = label_enc.fit_transform(X[col].astype(str))  # Convert to string if necessary

            # Scale numeric features
            scaler = StandardScaler()
            X[numeric_columns] = scaler.fit_transform(X[numeric_columns])

            # Train-Test Split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Initialize and train selected model
            if model_algorithm == "Random Forest":
                model = RandomForestClassifier(random_state=42)
            elif model_algorithm == "XGBoost":
                model = XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
            elif model_algorithm == "Neural Network":
                model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)

            # Fit the model
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)

            # Debugging: print model predictions and accuracy
            accuracy = accuracy_score(y_test, predictions)
            st.write(f"Accuracy Score: {accuracy}")

            # Checking if predictions and metrics are valid
            if predictions is not None and len(predictions) == len(y_test):
                st.success(f"Akurasi Model ({model_algorithm}): {accuracy:.2f}")
                st.write("Hasil Prediksi dan Aktual:")

                # Gabungkan nilai aktual dan prediksi dalam satu tabel
                result_df = pd.DataFrame({
                    'Aktual': y_test,
                    'Prediksi': predictions
                })

                # Tampilkan tabel
                st.write(result_df)
                
                # Confusion Matrix
                st.subheader("Confusion Matrix")
                cm = confusion_matrix(y_test, predictions)
                fig, ax = plt.subplots()
                ConfusionMatrixDisplay(cm).plot(ax=ax)
                st.pyplot(fig)

                # Classification Report
                st.subheader("Classification Report")
                report = classification_report(y_test, predictions, output_dict=True)
                st.dataframe(pd.DataFrame(report).transpose())

                # Feature Importance (if applicable)
                if model_algorithm in ["Random Forest", "XGBoost"]:
                    st.subheader("Feature Importance")
                    if model_algorithm == "Random Forest":
                        importances = model.feature_importances_
                    elif model_algorithm == "XGBoost":
                        importances = model.feature_importances_

                    # Plot feature importance
                    importance_df = pd.DataFrame({
                        'Feature': feature_columns,
                        'Importance': importances
                    }).sort_values(by='Importance', ascending=False)

                    st.bar_chart(importance_df.set_index('Feature'))
            else:
                st.error("Prediksi gagal")

            # Save the model and X_test to session_state
            st.session_state['model'] = model
            st.session_state['X_test'] = X_test  # Save X_test

            # Ensure the model directory exists
            model_path = "D:/aletta/KULIAH/Semester 7/Machine Learning/Praktikum/UAPTABULAR2/src/uaptabular2/model - Copy/my_model.joblib"
            if not os.path.exists(os.path.dirname(model_path)):
                os.makedirs(os.path.dirname(model_path))

            # Save model
            joblib.dump(model, model_path)  # Save MLP model using joblib

            st.success(f"Model disimpan sebagai '{model_path}'.")
        else:
            st.warning("Pilih kolom fitur dan target terlebih dahulu.")
    else:
        st.warning("Silakan unggah data yang sudah diproses terlebih dahulu.")
