import React from 'react';

import * as gsAi from "genericsuite-ai";

import { HomePage } from '../HomePage/HomePage.jsx';
import { AboutBody } from '../About/About.jsx';

import { Registry } from '../Registry/Registry.jsx';

// import { ExampleMainElement } from '../ExampleMenu/ExampleMainElement.jsx';
// import { ExampleChildElement } from '../ExampleMenu/ExampleChildElement.jsx';

const componentMap = {
    "AboutBody": AboutBody,
    "HomePage": HomePage,
    // "ExampleMainElement": ExampleMainElement,
    // "ExampleChildElement": ExampleChildElement,
};

export const App = () => {
    return (
        <gsAi.App
            appLogo="real-tor-logo-500.png"
            componentMap={componentMap}
        />
    );
}