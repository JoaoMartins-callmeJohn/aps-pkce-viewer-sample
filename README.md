# APS PKCE Viewer Sample

![platforms](https://img.shields.io/badge/platform-windows%20%7C%20osx%20%7C%20linux-lightgray.svg)
[![viewer](https://img.shields.io/badge/Viewer-v7-blue.svg)](https://aps.autodesk.com/en/docs/viewer/v7)
[![license](https://img.shields.io/:license-mit-green.svg)](https://opensource.org/licenses/MIT)

A single-page app that uses [PKCE OAuth flow](https://aps.autodesk.com/en/docs/oauth/v2/tutorials/get-3-legged-token-pkce/) to obtain a 3-legged token and then renders a design with [APS Viewer](https://aps.autodesk.com/en/docs/viewer/v7) — no server required.

[![Watch the demo](https://img.youtube.com/vi/_ApOJNtrCmg/0.jpg)](https://www.youtube.com/watch?v=_ApOJNtrCmg)

## Features

- **No server required** — the entire PKCE flow is handled client-side using `localStorage` and the browser's Web Crypto API.
- **Paste-and-go UI** — enter your Client ID and model URN directly in the browser and click Login.
- **APS Viewer integration** — once authenticated, the model is rendered immediately in the browser.

## How It Works

1. Enter your APS application **Client ID** and the **Model URN** in the form.
2. Click **Login** to start the PKCE authorization flow.
3. After authenticating with Autodesk, you are redirected back and the model is loaded in the Viewer.

## Prerequisites

- An [APS application](https://aps.autodesk.com/en/docs/oauth/v2/tutorials/create-app/) with `data:read` scope and the callback URL pointing to the hosted page (e.g., `https://joaomartins-callmejohn.github.io/aps-pkce-viewer-sample`).
- A URN of a model already translated via the [Model Derivative](https://aps.autodesk.com/en/docs/model-derivative/v2) service.
- The app [provisioned in your hub](https://get-started.aps.autodesk.com/#provision-access-in-other-products) if you need to access models from BIM 360 or ACC.

## Usage

### Try It Online

Visit **[https://joaomartins-callmejohn.github.io/aps-pkce-viewer-sample](https://joaomartins-callmejohn.github.io/aps-pkce-viewer-sample)**.

Add the URL above as a callback URL in your APS application settings, then enter your Client ID and model URN and click Login.

### Running Locally

1. Clone this repository:

    ```bash
    git clone https://github.com/JoaoMartins-callmeJohn/aps-pkce-viewer-sample.git
    cd aps-pkce-viewer-sample
    ```

2. Serve the files with any static HTTP server. The easiest option if you have Python installed is the included `server.py`, which automatically sets the callback URL to `http://localhost:8080/`:

    ```bash
    python server.py
    ```

    Alternatively, use any other static server:

    ```bash
    npx serve .
    ```

3. Add the local URL (e.g., `http://localhost:8080/`) as a callback URL in your APS application settings.

4. Open the served URL in your browser, enter your Client ID and model URN, and click **Login**.

## Provision Access in Other Products

If you want to view models from a specific hub (BIM 360, ACC, Fusion Team, etc.), your APS application must be provisioned. Follow the instructions at [https://get-started.aps.autodesk.com/#provision-access-in-other-products](https://get-started.aps.autodesk.com/#provision-access-in-other-products).

## License

This sample is licensed under the terms of the [MIT License](LICENSE). Refer to the `LICENSE` file for more details.

## Written by

João Martins [@JooPaulodeOrne2](http://twitter.com/JooPaulodeOrne2), [Developer Advocate](http://aps.autodesk.com)
