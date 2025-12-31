# Augmented Analytics Dashboard

An intelligent business intelligence dashboard that combines traditional data visualization with AI-powered insights, predictions, and automated analysis. Built with HTML/CSS/JavaScript frontend and Python/ML backend, integrated with Power BI for advanced data visualization.

## Features

### AI-Powered Analytics
- **Automated Insights**: AI generates actionable business insights from your data
- **Predictive Analytics**: Revenue forecasting and customer churn prediction
- **Smart Recommendations**: Data-driven suggestions for business optimization

### Advanced Visualizations
- **Power BI Integration**: Seamless embedding of Power BI reports
- **Interactive Charts**: Dynamic charts using Chart.js
- **Real-time KPIs**: Live dashboard with key performance indicators

### Business Intelligence
- **Multi-tab Interface**: Overview, Analytics, Predictions, and AI Insights
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Export Functionality**: Export insights and data for further analysis

## Technology Stack

### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with gradients and animations
- **JavaScript (ES6+)**: Interactive functionality and API integration
- **Chart.js**: Data visualization library
- **Power BI Client**: Microsoft Power BI embedding

### Backend
- **Python 3.8+**: Core backend language
- **Flask**: Web framework for API endpoints
- **Scikit-learn**: Machine learning models
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing

### Machine Learning Models
- **Random Forest Regressor**: Revenue prediction
- **Random Forest Classifier**: Customer churn prediction
- **Time Series Analysis**: Trend detection and forecasting

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Power BI account (optional, for full integration)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd augmented_dashboards
   ```

2. **Set up the backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

3. **Open the frontend**
   - Open `frontend/index.html` in your web browser
   - Or serve it using a local web server:
     ```bash
     cd frontend
     python -m http.server 8000
     ```
     Then visit `http://localhost:8000`

### Configuration

1. **Power BI Integration** (Optional)
   - Update `config/powerbi_config.json` with your Power BI credentials
   - Replace placeholder values with actual report IDs and embed URLs

2. **API Configuration**
   - Backend runs on `http://localhost:5000` by default
   - Update `frontend/script.js` if using different port

## Usage

### Dashboard Tabs

#### Overview
- **KPI Cards**: Revenue, Active Users, Orders, Conversion Rate
- **Power BI Reports**: Embedded interactive reports
- **Real-time Updates**: Live data refresh functionality

#### Analytics
- **Revenue Trends**: Line chart showing revenue over time
- **User Engagement**: Doughnut chart of user activity
- **Geographic Distribution**: Bar chart of regional data
- **Product Performance**: Radar chart comparing products

#### Predictions
- **Revenue Forecast**: ML-powered revenue predictions
- **Churn Analysis**: Customer churn risk assessment
- **Confidence Metrics**: Prediction reliability indicators

#### AI Insights
- **Automated Insights**: AI-generated business recommendations
- **Smart Analysis**: Pattern recognition and trend detection
- **Actionable Recommendations**: Data-driven business advice

### API Endpoints

- `GET /api/kpi-data` - Get current KPI metrics
- `GET /api/analytics-data` - Get analytics data for charts
- `GET /api/predictions` - Get ML predictions
- `GET /api/insights` - Get AI-generated insights
- `POST /api/generate-insights` - Generate new AI insights
- `GET /api/health` - Health check endpoint

## Customization

### Adding New Data Sources
1. Update `backend/app.py` to include new data processing
2. Modify the ML models to incorporate new features
3. Update the frontend to display new visualizations

### Styling Customization
- Modify `frontend/styles.css` for visual changes
- Update color schemes, fonts, and layouts
- Add new CSS animations and effects

### ML Model Enhancement
- Add new models in `backend/app.py`
- Implement additional prediction algorithms
- Enhance feature engineering for better accuracy

## Sample Data

The project includes sample datasets:
- `data/sample_sales.csv` - Sales transaction data
- `data/sample_customers.csv` - Customer information and churn risk

## Power BI Integration

### Setup Steps
1. Create a Power BI workspace
2. Upload your reports to Power BI
3. Generate embed tokens for your reports
4. Update the configuration file with your credentials
5. Replace the placeholder in the frontend with actual Power BI embedding code

### Required Permissions
- Power BI Pro or Premium license
- Workspace access permissions
- Report embedding permissions

## Troubleshooting

### Common Issues

1. **Backend not starting**
   - Check Python version (3.8+ required)
   - Install all dependencies: `pip install -r requirements.txt`
   - Check port 5000 is not in use

2. **Frontend not loading data**
   - Ensure backend is running on port 5000
   - Check browser console for API errors
   - Verify CORS settings in backend

3. **Power BI not displaying**
   - Verify Power BI credentials in config
   - Check embed URLs are correct
   - Ensure reports are published and accessible

### Debug Mode
- Backend runs in debug mode by default
- Check console logs for detailed error messages
- Use browser developer tools for frontend debugging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the API documentation

## Roadmap

- [ ] Real-time data streaming
- [ ] Advanced ML models (LSTM, XGBoost)
- [ ] Natural language query interface
- [ ] Mobile app version
- [ ] Multi-tenant support
- [ ] Advanced security features

---
