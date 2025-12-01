# Quickstart: Simple Expression Calculator

**Date**: 2025-12-01

This guide provides the steps to set up and run the Simple Expression Calculator application.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Setup

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```
    Activate the environment:
    - On Windows: `venv\Scripts\activate`
    - On macOS/Linux: `source venv/bin/activate`

3.  **Install the dependencies**:
    Create a `requirements.txt` file with the following content:
    ```
    streamlit
    ```
    Then, run the following command to install the packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  Make sure your virtual environment is activated.

2.  Run the Streamlit app from the root directory of the project:
    ```bash
    streamlit run app.py
    ```

3.  The application will open in your default web browser.

## How to Use

1.  Enter a mathematical expression (e.g., `5 + 2 * 3`) in the input box.
2.  Click the "Calculate" button.
3.  The result will be displayed on the screen.
