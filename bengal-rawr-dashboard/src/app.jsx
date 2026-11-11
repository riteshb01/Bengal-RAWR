import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Sidebar from './shared/components/Sidebar';
import MobileNav from './shared/components/MobileNav';
import AppRoutes from './routes';
import './styles/index.css';

function App() {
  return (
    <Router>
      <div className="app-shell">
        <Sidebar />
        <MobileNav />
        <main className="main-content">
          <AppRoutes />
        </main>
      </div>
    </Router>
  );
}

export default App;
