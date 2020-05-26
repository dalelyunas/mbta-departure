import React from 'react';


export const STATIONS = [
    {
        name: 'North Station',
        value: 'place-north'    
    },
    {
        name: 'South Station',
        value: 'place-sstat'
    }
];

function StationSelect(props) {
    return (
        <div>
            <select value={props.station} onChange={e => props.setStation(e.target.value)}>
                {STATIONS.map(station => <option key={station.value} value={station.value}>{station.name}</option>)}
            </select>
        </div>
    );
}

export default StationSelect;