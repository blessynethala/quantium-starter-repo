import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from dash.testing.application_runners import import_app


def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Check that the header (H1) is present and has the correct text
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"


def test_visualisation_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Check that the line chart (graph) is present
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Check that the region radio button picker is present
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None