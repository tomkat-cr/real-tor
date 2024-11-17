import React from 'react';

import * as gsAi from "genericsuite-ai";

import { HomePage } from '../HomePage/HomePage.jsx';
import { AboutBody } from '../About/About.jsx';

const componentMap = {
    "AboutBody": AboutBody,
    "HomePage": HomePage,
};

export const App = () => {
    return (
        <gsAi.App
            appLogo="real-tor-logo-circled-500.png"
            componentMap={componentMap}
        />
    );
}