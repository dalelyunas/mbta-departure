import { useState, useEffect } from 'react';

function fetchDepartures(station, setDepartures) {
    fetch(`/api/v1/stops/${station}/commuterRailDepartures`)
        .then(resp => resp.json())
        .then(data => setDepartures(data))
}

export function useDepartures(station) {
    let [departures, setDepartures] = useState([]);
    
    useEffect(() => {
        fetchDepartures(station, setDepartures);
        const interval = setInterval(() => {
            fetchDepartures(station, setDepartures);
        }, 30000);
        return () => clearInterval(interval);
      }, []);

    return departures;
}
