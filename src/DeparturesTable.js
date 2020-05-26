import React from 'react';
import { useDepartures } from './useDepartures';

import './DeparturesTable.css';

const HEADERS = ['Carrier', 'Time', 'Destination', 'Train #', 'Track #', 'Status'];

function DeparturesTable(props) {
    const departures = useDepartures(props.station);
    return (
        <div class='container'>
            <table>
                <thead>
                    <tr>
                        {HEADERS.map(header => <th>{header}</th>)}
                    </tr>
                </thead>
                <tbody>
                    {departures.map(departure => {
                        return <tr>
                            <td>{departure.carrier}</td>
                            <td>{new Date(departure.departureTime).toLocaleTimeString()}</td>
                            <td>{departure.destination}</td>
                            <td>{departure.train || 'TBA'}</td>
                            <td>{departure.track || 'TBA'}</td>
                            <td>{departure.status}</td>
                        </tr>
                    })}
                </tbody>
            </table>
        </div>
    );
}

export default DeparturesTable;