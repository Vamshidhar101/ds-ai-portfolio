import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# 1. Generate Dummy Data (Simulating Telecom Data)
print("Generating Synthetic Data...")
np.random.seed(42)
n_samples = 1000
data = pd.DataFrame({
    'customer_id': range(n_samples),
    'monthly_bill': np.random.uniform(30, 120, n_samples),
    'total_usage_gb': np.random.uniform(5, 100, n_samples),
    'contract_type': np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], n_samples),
    'calls_customer_support': np.random.randint(0, 10, n_samples),
    'churn': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]) # 30% Churn Rate
})

# 2. Preprocessing
print("Preprocessing Data...")
le = LabelEncoder()
data['contract_type'] = le.fit_transform(data['contract_type'])

X = data.drop(['churn', 'customer_id'], axis=1)
y = data['churn']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Model Training
print("Training Random Forest Model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 4. Evaluation
predictions = model.predict(X_test_scaled)
print("\nModel Performance:")
print(classification_report(y_test, predictions))
print(f"AUC Score: {roc_auc_score(y_test, predictions):.2f}")

# 5. Save Model
joblib.dump(model, 'churn_model.pkl')
print("\nModel saved as churn_model.pkl")