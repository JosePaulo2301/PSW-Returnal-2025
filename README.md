# Subscription Manager

The **Subscription Manager** is a Python application designed to consolidate and control expenses related to service subscriptions, such as Netflix, Globo Play, Amazon, StartPlus etc.. By centralizing this information, the application helps track and manage recurring costs more efficiently, providing insights and visualizations for better financial control.

This app is part of PSW-Returnal, training provided by pythonando.
  
---

## 🛠 Features

- **Add Subscription:** Register new subscriptions with details like company name, website, subscription date, and cost.
- **Remove Subscription:** Delete services that are no longer needed.
- **Calculate Total Costs:** Compute the total monthly cost of active subscriptions.
- **View Spending History:** Generate a chart showing expenses over the last 12 months.

---

## ⚙️ Technologies Used

- **SQLite**: A lightweight database for data storage.
- **SQLModel**: A Python ORM for managing database operations.
- **Matplotlib**: For generating charts and visualizing expenses.

---

## 🚀 How to Run

### Prerequisites

Ensure you have Python installed along with the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application
1. Clone the repository and navigate to the project directory.
2. Run the main script:
```
python app.py
```
3. Follow the on-screen menu to manage your subscriptions.

## 💾 Example Data

The application comes preloaded with some sample subscription data:
- Netflix
- Globo Play
- Amazon
- StartPlus


📊 Dependencies
Here is the list of Python packages used in the project:
```
annotated-types==0.7.0
contourpy==1.3.1
cycler==0.12.1
fonttools==4.55.3
greenlet==3.1.1
kiwisolver==1.4.8
matplotlib==3.10.0
numpy==2.2.1
packaging==24.2
pillow==11.1.0
pydantic==2.10.4
pydantic_core==2.27.2
pyparsing==3.2.1
python-dateutil==2.9.0.post0
six==1.17.0
SQLAlchemy==2.0.36
sqlmodel==0.0.22
typing_extensions==4.12.2

```

🌟 Future Improvements
- Add support for exporting data to a CSV file.
- Integrate with online payment gateways to fetch subscription data automatically.
- Include notifications for upcoming payments.

📧 Contact
If you have any questions or suggestions, feel free to reach out to us via email at support@subscriptionmanager.com.
