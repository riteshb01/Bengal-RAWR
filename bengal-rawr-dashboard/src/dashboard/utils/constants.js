/**
 * Bengal RAWR Dashboard — Constants
 *
 * API_BASE is read from the Vite env variable VITE_API_BASE_URL.
 * Set it in .env.local for development, or in your hosting platform for production.
 * Fallback: http://localhost:8000/api/v1
 */

export const API_BASE = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api/v1';

// Workload threshold — weeks above this are flagged as overloaded
export const WORKLOAD_THRESHOLD = 7;

// Event type display labels & colors for the UI
export const EVENT_TYPE_CONFIG = {
  homework:     { label: 'Homework',     color: '#60a5fa', weight: 1 },
  assignment:   { label: 'Assignment',   color: '#34d399', weight: 2 },
  quiz:         { label: 'Quiz',         color: '#a78bfa', weight: 2 },
  lab:          { label: 'Lab',          color: '#2dd4bf', weight: 2 },
  presentation: { label: 'Presentation', color: '#fb923c', weight: 3 },
  project:      { label: 'Project',      color: '#f472b6', weight: 3 },
  midterm:      { label: 'Midterm',      color: '#facc15', weight: 5 },
  exam:         { label: 'Exam',         color: '#f87171', weight: 5 },
  final:        { label: 'Final',        color: '#ef4444', weight: 8 },
  reading:      { label: 'Reading',      color: '#94a3b8', weight: 1 },
  other:        { label: 'Other',        color: '#cbd5e1', weight: 1 },
};

// Severity display config
export const SEVERITY_CONFIG = {
  low:      { label: 'Low',      color: '#facc15', icon: '⚡' },
  medium:   { label: 'Medium',   color: '#fb923c', icon: '⚠️' },
  high:     { label: 'High',     color: '#f87171', icon: '🔥' },
  critical: { label: 'Critical', color: '#ef4444', icon: '🚨' },
};
