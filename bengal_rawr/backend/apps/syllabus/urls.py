from django.urls import path
from apps.syllabus.views import (
    CourseListCreateView, CourseDetailView,
    UploadSyllabusView, ReprocessSyllabusView,
    EventListView, EventDetailView, VerifyEventView,
    ConflictListView, RunConflictAnalysisView,
    DashboardSummaryView, HeatmapDataView, WeeklyWorkloadView,
    SemanticSearchView, HealthCheckView,
)

app_name = 'syllabus'

urlpatterns = [
    # Health
    path('health/',                         HealthCheckView.as_view(),       name='health'),
    # Courses
    path('courses/',                        CourseListCreateView.as_view(),  name='course-list'),
    path('courses/<int:pk>/',               CourseDetailView.as_view(),      name='course-detail'),
    # Syllabus upload & reprocessing
    path('upload-syllabus/',                UploadSyllabusView.as_view(),    name='upload-syllabus'),
    path('syllabi/<int:pk>/reprocess/',     ReprocessSyllabusView.as_view(), name='reprocess-syllabus'),
    # Events
    path('events/',                         EventListView.as_view(),         name='event-list'),
    path('events/<int:pk>/',                EventDetailView.as_view(),       name='event-detail'),
    path('events/<int:pk>/verify/',         VerifyEventView.as_view(),       name='event-verify'),
    # Conflicts
    path('conflicts/',                      ConflictListView.as_view(),      name='conflict-list'),
    path('conflicts/analyze/',              RunConflictAnalysisView.as_view(), name='conflict-analyze'),
    # Dashboard
    path('dashboard/',                      DashboardSummaryView.as_view(),  name='dashboard-summary'),
    path('dashboard/heatmap/',              HeatmapDataView.as_view(),       name='dashboard-heatmap'),
    path('dashboard/weekly-workload/',      WeeklyWorkloadView.as_view(),    name='dashboard-weekly-workload'),
    # Semantic search
    path('search/',                         SemanticSearchView.as_view(),    name='semantic-search'),
]
