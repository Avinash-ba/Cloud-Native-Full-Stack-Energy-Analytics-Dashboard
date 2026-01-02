import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line, Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import './App.css';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function App() {
  const [energyData, setEnergyData] = useState([]);
  const [summary, setSummary] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
    fetchSummary();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/v1/data');
      setEnergyData(response.data);
    } catch (error) {
      console.error('Error fetching energy data:', error);
    }
  };

  const fetchSummary = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/v1/summary/daily');
      setSummary(response.data);
    } catch (error) {
      console.error('Error fetching summary:', error);
    } finally {
      setLoading(false);
    }
  };

  const generateMockData = async () => {
    try {
      await axios.post('http://localhost:8000/api/v1/data/generate', { count: 20 });
      fetchData();
      fetchSummary();
    } catch (error) {
      console.error('Error generating mock data:', error);
    }
  };

  const chartData = {
    labels: energyData.map(d => new Date(d.timestamp).toLocaleTimeString()),
    datasets: [
      {
        label: 'Energy Consumption (kWh)',
        data: energyData.map(d => d.consumption),
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Energy Consumption Over Time',
      },
    },
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Energy Analytics Dashboard</h1>
      </header>
      <main>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <>
            <div className="summary">
              <h2>Daily Summary</h2>
              <p>Total Consumption: {summary.total_consumption?.toFixed(2)} kWh</p>
              <p>Average Consumption: {summary.average_consumption?.toFixed(2)} kWh</p>
              <p>Peak Consumption: {summary.peak_consumption?.toFixed(2)} kWh</p>
            </div>
            <button onClick={generateMockData}>Generate Mock Data</button>
            <div className="chart-container">
              <Line options={chartOptions} data={chartData} />
            </div>
          </>
        )}
      </main>
    </div>
  );
}

export default App;
