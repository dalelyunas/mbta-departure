import React, { useState } from 'react';

import DeparturesTable from './DeparturesTable';
import Clock from './Clock';
import StationSelect, { STATIONS } from './StationSelect';

import './App.css';

function App() {
  const [station, setStation] = useState(STATIONS[0])

  return (
    <div className="app">
      <div class=''>
        <Clock />
        <StationSelect station={station} setStation={setStation} />
      </div>
      
      <h1>Commuter Rail Departures</h1>
      <DeparturesTable station={station} />
    </div>
  );
}

export default App;
