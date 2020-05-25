import { useState, useEffect } from 'react';

function fetchDepartures(stopId, setDepartures) {
    fetch(`/api/v1/stops/${stopId}/commuterRailDepartureBoard`)
        .then(resp => resp.json())
        .then(data => setDepartures(data))
}

export function useDepartures(stopId) {
    let [departures, setDepartures] = useState([]);
    
    useEffect(() => {
        fetchDepartures(stopId, setDepartures)
        const interval = setInterval(() => {
            fetchDepartures(stopId, setDepartures)
        }, 20000);
        return () => clearInterval(interval);
      }, []);

    return departures;
}
