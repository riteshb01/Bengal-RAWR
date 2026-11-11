import React, { Suspense, lazy } from 'react';
import { Routes, Route } from 'react-router-dom';

const DashboardPage = lazy(() => import('../pages/DashboardPage'));
const CoursesPage   = lazy(() => import('../pages/CoursesPage'));
const EventsPage    = lazy(() => import('../pages/EventsPage'));
const TimelinePage  = lazy(() => import('../pages/TimelinePage'));
const ConflictsPage = lazy(() => import('../pages/ConflictsPage'));
const WorkloadPage  = lazy(() => import('../pages/WorkloadPage'));
const InsightsPage  = lazy(() => import('../pages/InsightsPage'));
const SettingsPage  = lazy(() => import('../pages/SettingsPage'));
const UploadPage    = lazy(() => import('../pages/UploadPage'));
const NotFoundPage  = lazy(() => import('../pages/NotFoundPage'));

const RouteFallback = () => (
  <div className="dashboard-loading" style={{ minHeight: '40vh' }}>
    <div className="spinner" />
  </div>
);

const AppRoutes = () => (
  <Suspense fallback={<RouteFallback />}>
    <Routes>
      <Route path="/"          element={<DashboardPage />} />
      <Route path="/courses"   element={<CoursesPage />} />
      <Route path="/events"    element={<EventsPage />} />
      <Route path="/timeline"  element={<TimelinePage />} />
      <Route path="/conflicts" element={<ConflictsPage />} />
      <Route path="/workload"  element={<WorkloadPage />} />
      <Route path="/insights"  element={<InsightsPage />} />
      <Route path="/settings"  element={<SettingsPage />} />
      <Route path="/upload"    element={<UploadPage />} />
      <Route path="*"          element={<NotFoundPage />} />
    </Routes>
  </Suspense>
);

export default AppRoutes;
