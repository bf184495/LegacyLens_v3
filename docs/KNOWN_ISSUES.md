# Known Issues

## Current

No critical open issues.

## Historical Issues

### Home Navigation Failure

Problem:
Returning to Home caused deleted widget errors.

Cause:
QMainWindow.setCentralWidget() destroyed the
previous HomeView instance.

Resolution:
Migrated navigation to QStackedWidget.

Status:
Resolved