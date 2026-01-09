<h1 align="center">📊 Customer Churn Analysis – Exploratory Data Analysis (EDA)</h1>

<hr>

<h2>📌 Project Overview</h2>
<p>
This project analyzes <b>customer churn behavior</b> in a telecommunications dataset to identify
the <b>key factors driving customer attrition</b>.  
Using <b>Exploratory Data Analysis (EDA)</b> with <b>Matplotlib</b>, the project uncovers churn
patterns across demographics, services, contracts, billing methods, tenure, and regions.
</p>

<p>
The insights from this analysis help telecom companies design
<b>data-driven customer retention strategies</b>.
</p>

<hr>

<h2>📂 Dataset Description</h2>
<ul>
  <li><b>Total Customers:</b> 7,043</li>
  <li><b>Target Variable:</b> Churn (Yes / No)</li>
  <li><b>Total Features:</b> 23</li>
</ul>

<h3>Key Attributes</h3>
<ul>
  <li><b>Demographics:</b> Gender, SeniorCitizen, Partner, Dependents, Region</li>
  <li><b>Services:</b> PhoneService, InternetService, MultipleLines, Streaming & Security Services</li>
  <li><b>Account Info:</b> Tenure, Contract, PaymentMethod, MonthlyCharges, TotalCharges</li>
  <li><b>Service Providers (SIM):</b> Airtel, Jio, BSNL, Vi</li>
</ul>

<h3>Churn Distribution</h3>
<ul>
  <li><b>Retained:</b> 5,174 (73.5%)</li>
  <li><b>Churned:</b> 1,869 (26.5%)</li>
</ul>

<p>The dataset is well-balanced by gender and suitable for churn analysis.</p>

<hr>

<h2>📁 Project Structure</h2>
<pre>
Customer-Churn-EDA/
│
├── Customer_churn.csv        # Dataset
├── main.py                   # EDA execution script
├── ploting.py                # Visualization logic
├── log_code.py               # Logging configuration
├── logs/                     # Auto-generated log files
└── README.md                 # Project documentation
</pre>

<hr>

<h2>⚙️ Technology Stack</h2>
<ul>
  <li>Python</li>
  <li>Pandas & NumPy</li>
  <li>Matplotlib (No Seaborn)</li>
  <li>Logging Module</li>
</ul>

<hr>

<h2>▶️ How to Run the Project</h2>

<ol>
  <li><b>Clone the repository</b></li>
</ol>

<pre>
git clone &lt;your-repo-url&gt;
cd Customer-Churn-EDA
</pre>

<ol start="2">
  <li><b>Install dependencies</b></li>
</ol>

<pre>
pip install pandas numpy matplotlib
</pre>

<ol start="3">
  <li><b>Run the analysis</b></li>
</ol>

<pre>
python main.py
</pre>

<p>
All visualizations will be generated sequentially, and logs will be stored automatically.
</p>

<hr>

<h2>📈 Exploratory Data Analysis (EDA)</h2>
<p>
EDA was performed using <b>Matplotlib only</b> to maintain full control over visualization clarity.
Each plot includes <b>exact customer counts</b> and percentages where applicable.
</p>

<h3>Visual Analyses Performed</h3>
<ul>
  <li>Gender × SeniorCitizen × Churn</li>
  <li>PhoneService × Gender × SeniorCitizen × Churn</li>
  <li>MultipleLines × Gender × Churn</li>
  <li>InternetService × SIM</li>
  <li>SIM × Gender × SeniorCitizen</li>
  <li>Service Usage Percentage</li>
  <li>Contract × SIM × Gender × Churn</li>
  <li>PaperlessBilling × Gender × Churn</li>
  <li>PaymentMethod × Gender × Churn</li>
  <li>Tenure (Quarter-based) × SIM × Gender × Churn</li>
  <li>MonthlyCharges × SIM × Churn</li>
  <li>Region × Gender × SeniorCitizen × Churn</li>
</ul>

<hr>

<h2>🔍 Key Insights</h2>

<h3>🔴 Early Tenure Churn</h3>
<ul>
  <li>Majority of churn occurs within the <b>first 0–6 months</b></li>
  <li>Churn drops sharply after customers cross <b>1 year tenure</b></li>
</ul>

<h3>📄 Contract & Payment Impact</h3>
<ul>
  <li><b>Month-to-Month contracts</b> have the highest churn</li>
  <li><b>1-Year & 2-Year contracts</b> show strong retention</li>
  <li><b>Electronic Check</b> users churn the most</li>
  <li><b>Auto-payment methods</b> show low churn</li>
</ul>

<h3>🌐 Service-Specific Findings</h3>
<ul>
  <li><b>Fiber Optic</b> has higher churn despite high usage</li>
  <li>Security & support services have <b>low adoption</b></li>
  <li>Streaming services show higher engagement</li>
</ul>

<h3>👥 Demographic & Regional Insights</h3>
<ul>
  <li><b>Senior citizens</b> churn more than non-seniors</li>
  <li><b>Gender has no significant impact</b> on churn</li>
  <li>Regional differences are minor</li>
</ul>

<hr>

<h2>📊 Overall Summary</h2>
<ul>
  <li><b>Churn Rate:</b> 26.5%</li>
  <li><b>Retained Customers:</b> 73.5%</li>
  <li><b>Primary Churn Drivers:</b>
    <ul>
      <li>Early tenure dissatisfaction</li>
      <li>Month-to-Month contracts</li>
      <li>Manual payment methods</li>
      <li>Fiber optic service issues</li>
      <li>Low adoption of value-added services</li>
    </ul>
  </li>
</ul>

<p>
Customer churn is <b>predictable and preventable</b> with targeted early-stage interventions.
</p>

<hr>

<h2>🚀 Future Enhancements</h2>
<ul>
  <li>Predictive churn modeling</li>
  <li>Feature importance analysis</li>
  <li>Retention strategy simulation</li>
  <li>Dashboard integration</li>
</ul>

<hr>

<h2>✍️ Author</h2>
<p>
<b>Bala Venu</b><br>
Data Analyst | Python | EDA | Data Visualization
</p>
