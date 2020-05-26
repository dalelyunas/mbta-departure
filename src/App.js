import React, { useState } from 'react';

import DeparturesTable from './DeparturesTable';
import StationSelect, { STATIONS } from './StationSelect';

import styles from './App.module.css';

function App() {
  const [station, setStation] = useState(STATIONS[0].value)

  return (
    <div className={styles.app}>
      <StationSelect station={station} setStation={setStation} />
      <h3>Commuter Rail Departures</h3>
      <DeparturesTable station={station} />
    </div>
  );
}

export default App;
