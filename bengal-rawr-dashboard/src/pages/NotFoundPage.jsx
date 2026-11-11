import React from 'react';
import { Link } from 'react-router-dom';

const NotFoundPage = () => {
  return (
    <div className="page">
      <div className="card" style={{ marginTop: '3rem', textAlign: 'center', padding: '3rem 1.5rem' }}>
        <p className="page-eyebrow">404</p>
        <h1 className="page-title" style={{ marginBottom: '0.75rem' }}>Page Not Found</h1>
        <p className="page-subtitle" style={{ marginBottom: '1.75rem' }}>
          The route you requested does not exist.
        </p>
        <Link to="/" className="upload-btn" style={{ display: 'inline-block', textDecoration: 'none' }}>
          Return to Dashboard
        </Link>
      </div>
    </div>
  );
};

export default NotFoundPage;

